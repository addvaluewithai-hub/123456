# T-TREC-PACKAGE-AUDIT — Thermally regenerative electrochemical package audit

Branch: `TREC-01`
Status: ready
Seeded by: R078
Recommended role: `computational-modeler`

## Why this task exists

R078 found a credible independent low-grade-heat branch that is not blocked on the WET-01 or TO-01 hardware experiments. Recent experiments report thermally regenerative electrochemical battery/cycle performance around one-third of Carnot under optimized electrolyte conditions, but power density and thermal-regeneration/package duty remain the practical uncertainty.

## Mission

Build a source-to-electric/package screen for a 20→60 °C low-grade heat source using experimentally anchored TREC/TREB data. Do not optimize chemistry; first determine whether a 10 W DC / <=2 L architecture is even compatible with measured mass/power density plus realistic heat recuperation and cycling hardware.

## Required anchors

- Applied Energy 2025 experimental TREB: max relative Carnot efficiency 33.52% and peak power density 12.85 mW/g at optimized dimensionless electrolyte parameter Θ; heat recovery remains important.
- J. Mater. Chem. A 2025 charging-free TREC: 2.42% absolute efficiency without heat recuperation and 4.29% with 50% heat recuperation between 20 and 60 °C.
- Nature Communications 2014 CuHCF/Cu TREC: experimental cycle and heat-recuperation methodology; 3.7% cycle efficiency between 10 and 60 °C without recuperation and projected/test-supported improvement with recuperation.

## Quantitative gate

At 20→60 °C, Carnot is ~12.01%. The 33.52%-of-Carnot experimental point corresponds to ~4.03% absolute heat-to-electric efficiency. At 12.85 mW/g, 10 W requires ~778 g of the mass basis used by that paper before heat exchangers, containment, thermal switching/flow hardware and power electronics are charged.

The audit must therefore report:

1. what mass the 12.85 mW/g denominator actually includes;
2. cycle time / average versus peak power normalization;
3. hot/cold heat per cycle and required recuperation effectiveness;
4. active-material/electrolyte volume at measured density;
5. heat-exchanger + thermal-switch/flow volume and parasitic power;
6. net DC power and complete package volume;
7. absolute efficiency and fraction of Carnot;
8. fair comparison with WET-01 and TO-01 at the same 40 K source span.

## Success / falsification test

`PROMISING` only if an experimentally anchored envelope can project >=10 W net DC in <=2 L at >=15% Carnot without assuming unmeasured near-perfect heat recuperation or treating peak cell power as steady module power. Otherwise quantify the exact mass/thermal-cycling term that misses the target and mark LOW PRIORITY or NEEDS DATA.

## Evidence URLs

- https://doi.org/10.1016/j.apenergy.2025.126703
- https://doi.org/10.1039/D5TA03351A
- https://doi.org/10.1038/ncomms4942
