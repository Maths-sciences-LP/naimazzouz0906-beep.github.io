/**
 * drawTree — Arbre de probabilités avec D3.js
 *
 * Usage :
 *   drawTree("container-id", branches, options?)
 *
 * branches : tableau de branches niveau 1, chaque branche :
 *   { name, color, p, children: [{ name, color, p, leaf?, leafP? }] }
 *
 *   p: null  → champ de saisie vide (input)
 *   p: "0,6" → valeur pré-remplie (texte)
 *   p: undefined → rien affiché
 *
 *   leaf: "V∩G"  → étiquette au bout du chemin
 *   leafP: null   → champ de saisie pour le produit du chemin
 *   leafP: "0,03" → valeur pré-remplie
 *
 * options :
 *   width  (défaut 580)
 *   height (défaut 240)
 *   rootLabel (défaut "Départ")
 *
 * Dépendance : D3.js v7 (https://cdn.jsdelivr.net/npm/d3@7)
 */
(function () {
  "use strict";

  function drawTree(containerId, branches, opts) {
    opts = opts || {};
    var W = opts.width || 580;
    var H = opts.height || 240;
    var rootLabel = opts.rootLabel !== undefined ? opts.rootLabel : "Départ";
    var ml = 55, mr = 130, mt = 22, mb = 22;
    var iw = W - ml - mr;
    var ih = H - mt - mb;

    /* Hierarchy */
    var rootData = { name: rootLabel, children: branches };
    var root = d3.hierarchy(rootData);
    d3.tree().size([ih, iw])(root);

    /* SVG */
    var el = document.getElementById(containerId);
    if (!el) return;
    el.innerHTML = "";
    var svg = d3.select(el).append("svg")
      .attr("viewBox", "0 0 " + W + " " + H)
      .attr("width", "100%")
      .style("max-width", W + "px")
      .style("display", "block")
      .style("margin", "14px auto")
      .style("background", "#fff")
      .style("border", "1px solid #e2e8f0")
      .style("border-radius", "8px")
      .style("padding", "8px")
      .style("font-family", "'Segoe UI', system-ui, sans-serif");

    var g = svg.append("g").attr("transform", "translate(" + ml + "," + mt + ")");

    /* ---- Links + probabilities on branches ---- */
    root.links().forEach(function (link) {
      var s = link.source, t = link.target;
      var col = t.data.color || "#555";
      var sw = t.depth === 1 ? 2.2 : 1.8;

      g.append("line")
        .attr("x1", s.y).attr("y1", s.x)
        .attr("x2", t.y).attr("y2", t.x)
        .attr("stroke", col).attr("stroke-width", sw);

      /* Midpoint + perpendicular offset (above branch) */
      var mx = (s.y + t.y) / 2;
      var my = (s.x + t.x) / 2;
      var dx = t.y - s.y, dy = t.x - s.x;
      var len = Math.sqrt(dx * dx + dy * dy) || 1;
      var offx = (-dy / len) * 15;
      var offy = (dx / len) * 15;

      if (t.data.p === null) {
        /* Empty input field */
        var fo = g.append("foreignObject")
          .attr("x", mx + offx - 24).attr("y", my - offy - 13)
          .attr("width", 48).attr("height", 22);
        fo.append("xhtml:input")
          .attr("type", "text")
          .attr("class", "bi tree-bi")
          .attr("style",
            "width:42px;text-align:center;font-size:11px;" +
            "border:1.5px solid " + col + ";border-radius:4px;" +
            "padding:1px 2px;background:#fff;color:#2d3748");
      } else if (t.data.p !== undefined) {
        g.append("text")
          .attr("x", mx + offx).attr("y", my - offy)
          .attr("text-anchor", "middle")
          .attr("fill", col).attr("font-size", 11)
          .text(t.data.p);
      }
    });

    /* ---- Nodes ---- */
    root.descendants().forEach(function (d) {
      var isRoot = d.depth === 0;
      var isLeaf = !d.children;
      var col = d.data.color || "#0969da";
      var r = isRoot ? 8 : (isLeaf ? 5 : 7);

      g.append("circle")
        .attr("cx", d.y).attr("cy", d.x)
        .attr("r", r).attr("fill", col);

      /* Node label */
      if (d.data.name) {
        if (isRoot) {
          g.append("text")
            .attr("x", d.y).attr("y", d.x + 22)
            .attr("text-anchor", "middle")
            .attr("fill", "#2d3748").attr("font-size", 10)
            .attr("font-weight", "bold")
            .text(d.data.name);
        } else if (!isLeaf) {
          g.append("text")
            .attr("x", d.y + 12).attr("y", d.x + 5)
            .attr("fill", col).attr("font-size", 13)
            .attr("font-weight", "bold")
            .text(d.data.name);
        }
      }

      /* Leaf: name + result label + probability */
      if (isLeaf) {
        var lx = d.y + 10;

        /* Event name at leaf */
        if (d.data.name && !d.data.leaf) {
          g.append("text")
            .attr("x", lx).attr("y", d.x + 4)
            .attr("fill", col).attr("font-size", 12)
            .attr("font-weight", "bold")
            .text(d.data.name);
        }

        /* Result label (e.g. "V∩G") */
        if (d.data.leaf) {
          g.append("text")
            .attr("x", lx).attr("y", d.x - 3)
            .attr("fill", "#2d3748").attr("font-size", 11)
            .attr("font-weight", "bold")
            .text(d.data.leaf);

          if (d.data.leafP === null) {
            var fo2 = g.append("foreignObject")
              .attr("x", lx).attr("y", d.x + 2)
              .attr("width", 72).attr("height", 20);
            fo2.append("xhtml:input")
              .attr("type", "text")
              .attr("class", "bi tree-bi")
              .attr("style",
                "width:66px;font-size:10px;" +
                "border:1.5px solid " + col + ";border-radius:4px;" +
                "padding:1px 3px;background:#fff;color:#2d3748");
          } else if (d.data.leafP) {
            g.append("text")
              .attr("x", lx).attr("y", d.x + 12)
              .attr("fill", "#718096").attr("font-size", 10)
              .text(d.data.leafP);
          }
        }
      }
    });
  }

  /* Expose globally */
  window.drawTree = drawTree;
})();
