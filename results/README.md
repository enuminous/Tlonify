# Exploratory simulation records — 2026-11-25

Source model: commit d8f07b07ef7553996cd52f5a05d9d67039dc6d78, simulation.py blob 2bc5ca00595b5ad3492b9ac70f4b2f86a1bf6cb5.

- [TLON-SIM-001](TLON-SIM-001/summary.json): 8,575 configurations, 3,438,575 states, no invariant violations in grid. Original Python session reported four passing unit tests. 3,298 high-risk cases at step 400. 667/1,715 zero-new-mismatch cases scored >=0.70.
- [EFMW-TLON-002](EFMW-TLON-002/summary.json): 560 configurations, 224,560 sweep states; 204 zero final backlog, 232 risk >=0.75. Claim generation g=12 is arbitrary, not measured. Seven scenarios separate from sweep counts.

Published numerical datasets are regenerated with an equivalent JavaScript translation of the pinned Python recurrence, not byte-identical copies of the original local Python exports. Full preset trajectories and split sweep endpoints are retained. The Python reproduction runner regenerates both experiments. No new empirical data, independent review, or approval is claimed. Seven scientific experiments in PROTOCOL.md remain proposed.

Original local artifact SHA256 (not published byte-for-byte): EFMW-TLON-002.json 4b7ab32a4c2afb8172a03407a3ae578efb8c3c2e9819aa60c9ef800580594346; Tlonify-SIM-001.zip a859ae1946f79cc3665986e59fd8f76d90d44846fc3c3380bb6e20060c6b86b5; sweep.csv a5ccbd59eb1e43f2dc374da771b16743323c396b8c3dbc7b408987389753db10.
