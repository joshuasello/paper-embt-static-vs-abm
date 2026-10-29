# Revisions plan: supervisor feedback, round 2

- **Source of feedback:** `Joshua_PhD_Thesis_red.pdf` (Thinus Booysen), comments on Chapter 8 of the thesis build.
- **Branch:** `supervisor-revisions-round2`
- **Scope:** comments #41 to #58, which fall on this paper (thesis PDF pp. 171 to 214). Comments #1 to #40 concern the thesis front matter, Chapter 1 and the other chapters, and are handled in the thesis repo. The one exception carried over is the "corridors" terminology of #4 (see Cross-cutting B under #42).
- **Edit target:** `main.tex` and `appendix.tex` in this repo are the source. After the edits, re-sync into `thesis/phd-thesis/replay_vs_abm/replay_vs_abm.tex` (see Cross-cutting C under #47).
- **Page numbers:** "PDF p." is the page of the feedback PDF; "printed p." is the thesis page number (PDF p. minus 24). Thesis section 8.x is section x of the paper; thesis Table 8.n is Table n of the paper. Line numbers refer to the source at commit `1e8d685` and will drift as edits are made.
- **Self-review:** 20 further points, found after the supervisor's comments were applied, are recorded at the end ("Self-review").
- **Comment numbers** follow the order of extraction from the PDF. #48 is a second note on the same table as #47 and is handled there.

## Index

| # | PDF p. | Location | Topic | Status |
|---|---|---|---|---|
| 41 | 171 | Abstract | "infrastructure that is selected" is ambiguous | [x] |
| 42 | 171 | Abstract | ICE competitor sentence; terminology sweeps (A, B) | [x] |
| 43 | 171 | Abstract | "assumptions or information about passenger demand" | [x] |
| 44 | 177 | §2.4 | Misplaced "they"; claim conflicts with Table 1 | [x] |
| 45 | 177 | §2.4 | Why only $M_A$ has ICE competitors | [x] |
| 46 | 178 | Table 1 | Separate the "This study" row | [x] |
| 47, 48 | 180 | Table 2 | Text too small; sync and verify (C) | [x] (C open) |
| 49 | 182 | §4.1 | ICE vehicles are also agents | [x] |
| 50 | 182 | §4.1 | "electrify the same observed vehicles" | [x] |
| 51 | 182 | §4.1 | "recorded dwell periods" | [x] |
| 52 | 182 | Table 4 | "The agents of the community / The same agents" | [x] |
| 53 | 182 | Table 4 | "Other vehicles: None" | [x] |
| 54 | 192 | Table 5 | Praise; supports #55 | n/a |
| 55 | 192 | Table 5 | Move the measures before the method detail | [x] |
| 56 | 192 | Table 5 | "Front" is unclear | [x] |
| 57 | 208 | Table 20 | Text overlaps in the first column | [x] |
| 58 | 214 | Appendix A | Broken references `[?]` | [ ] (Joshua) |

---

## #41 Abstract: "infrastructure that is selected"

- [x] Done
- **Where:** PDF p. 171, printed p. 147, Abstract. `main.tex:52` (abstract), `main.tex:101` (research gap), `main.tex:109` (RQ2).
- **Marked:** "...changes the charging infrastructure that is selected."
- **Comment:** "This wording actually bothered me in Chapter 1 too - it is ambiguous about the act of selection. I think what you could consider using is 'A key question remains: does using a fleet simulation model, in which drivers' decision making and agency are explicitly included, suggest a different infrastructure configuration'."
- **Decision:** Reword the framing text (abstract, research gap, RQ2) along his lines. Keep "selected design", "selection rule", $\mathbf{x}^\star_R$ and $\mathbf{x}^\star_A$ in Methods and Results, where the selection rule of each model defines the act of selecting.
- **Proposed wording:**
  - Abstract.
    Old: "However, it remains unclear whether introducing explicit representations of driver agency changes the charging infrastructure that is selected."
    New: "However, it remains unclear whether a fleet simulation model in which drivers' decision-making and agency are explicit suggests a different charging infrastructure configuration."
  - Research gap.
    Old: "...and whether infrastructure selected under fixed-mobility assumptions remains effective once drivers respond endogenously and compete for passengers with the internal-combustion vehicles that share their corridors."
    New: "...and whether a charging design suggested by a fixed-mobility model remains effective once drivers respond endogenously and compete for passengers with the internal-combustion vehicles that share their routes."
  - RQ2.
    Old: "Does endogenous driver behaviour change the charging infrastructure that is selected when each model is evaluated using the outcomes it can validly represent?"
    New: "Does a model in which drivers' decisions are explicit suggest a different charging infrastructure configuration from a data-replay model, when each model judges designs by the outcomes it can validly represent?"
- **Reply:** Agreed. The abstract, research gap and RQ2 now ask whether the agent-based model suggests a different infrastructure configuration. "Selected" remains only in the Methods and Results, where each model's selection rule defines it.

## #42 Abstract: ICE competitor sentence

- [x] Done
- **Where:** PDF p. 171, printed p. 147, Abstract. `main.tex:52`.
- **Marked:** "while the agent-based model also represents synthetic internal combustion engine vehicles competing for passengers on the same corridors"
- **Comment:** "Not clear at this point yet why this is necessary, and how it is apples with apples. Since it is just the abstract, it may make sense to rather just remove this contentious sentence."
- **Decision:** Keep the clause but reword it so that it says why the competitors are there. The later abstract sentences on "internal-combustion counterfactuals" and the 85% to 98% capture share depend on it. The like-for-like argument goes in §4.1 (#45).
- **Proposed wording:**
  Old: "Both models electrify the same observed vehicles, while the agent-based model also represents synthetic internal combustion engine vehicles competing for passengers on the same corridors."
  New: "Both models electrify the same observed vehicles. The agent-based model also simulates the internal combustion engine (ICE) taxis on the same routes, which can carry the passengers that an electric vehicle misses while it charges."
  Then use "ICE" in the later abstract sentences.
- **Reply:** I kept a shorter version, because the abstract's passenger results depend on the competitors. It now states why they are there: they can take the passengers an EV misses while it charges. Section 4.1 now explains why only the agent-based model has them and why the comparison is still like-for-like.

### Cross-cutting A: EV agents, ICE competitors, observed EVs

The paper uses "agents" for the observed vehicles in the text, but for all simulated drivers in Table 6 (the "Agents" column of 1,358, 1,673 and 686). Table 4 then says "The agents of the community / The same agents" (#52). Rules for the whole paper:

- [x] In $M_A$: **EV agents** are the qualified observed vehicles, electrified. **ICE competitors** are their synthetic copies. **Drivers** means all of them.
- [x] In the paired ICE counterfactual: "the EV agents in their ICE counterfactual" (not "the observed agents operate as ICE vehicles").
- [x] In $M_R$: **observed EVs** for the replayed vehicles as EVs; **observed ICEVs** where the text means their recorded ICE operation.
- [x] Table 6 (`tab:models`, `main.tex:597-608`): rename the column "Agents" to "Drivers"; in the caption, "Drivers: the EV agents and their ICE competitors in \MA, with the scale factor $k$."
- [x] Sweep `main.tex` and `appendix.tex` for "agent", "copies", "synthetic ICE" and "observed vehicles", and apply the rules.

### Cross-cutting B: corridors → routes (from #4)

"Corridor" has a specific meaning in civil engineering, and most examiners are civil engineers.

- [x] **Loose uses, change to "routes"** (or rephrase, e.g. "the full corridor population" → "all drivers on these routes"):
  `main.tex:52, 101, 111, 116, 151, 170` (second use: "the hubs and corridors that they share"), `278` ("residential ends of corridors"), `307, 358, 442`; `appendix.tex:79` ("a corridor is a property of the operation").
- [x] **Keep, external uses:** `main.tex:147` (MATSim study), `170` (first use: other studies' units of analysis), `266, 281`; `appendix.tex:274, 290` (CITP surveyed corridors).
- [x] **Keep, technical term:** `main.tex:383`; `appendix.tex:23, 28, 49`. Here a corridor is defined as "an undirected pair of consecutive anchor dwells that recurs on at least three vehicle-days and two dates" (community test, Table A1).
- [x] Also update the LaTeX `% Discuss` comments where convenient (not required).

## #43 Abstract: passenger demand

- [x] Done
- **Where:** PDF p. 171, printed p. 147, Abstract, last paragraph. `main.tex:52`.
- **Marked:** "passe[nger]"
- **Comment:** "assumptions or information about passenger demand"
- **Decision:** Adopt his wording.
- **Proposed wording:**
  Old: "...and explicit assumptions about driver behaviour and passenger demand."
  New: "...and explicit assumptions about driver behaviour and assumptions or information about passenger demand."
- **Reply:** Done.

## #44 §2.4: "they" and the mixed-fleet claim

- [x] Done
- **Where:** PDF p. 177, printed p. 153, §2.4, paragraph before Table 1. `main.tex:180`.
- **Marked:** "and outside scheduling studies they have not placed EVs in a mixed fleet"
- **Comment:** "something wrong here - I think 'they' is misplaced?"
- **Also found:** The claim conflicts with Table 1, which lists our earlier agent-based model (`sello2025_stellenbosch_embt_abm`) as adaptive with ICE competition = Yes.
- **Decision:** Name our earlier model as the exception.
- **Proposed wording:**
  Old: "Behavioural models let drivers adapt, but they have not been compared with replay on the same vehicles, and outside scheduling studies they have not placed EVs in a mixed fleet."
  New: "Behavioural models let drivers adapt, but they have not been compared with replay on the same vehicles. Scheduling studies place EVs in a mixed fleet without competition, and only \citet{sello2025_stellenbosch_embt_abm} has simulated EVs that compete with ICE vehicles for passengers."
- **Reply:** Fixed. "They" was ambiguous. The sentence now separates the scheduling studies from our earlier agent-based model, which is the one exception, consistent with Table 1.

## #45 §2.4: why only $M_A$ has ICE competitors

- [x] Done
- **Where:** PDF p. 177, printed p. 153, §2.4 heading "Comparing models of different structure". Section at `main.tex:172-176`; new paragraph in §4.1 at `main.tex:307`.
- **Comment:** "I was expecting here to see the explanation of why the ABM has petrol competitors and the replay apparently not. Maybe it is still coming. Will check."
- **Decision:** Put the explanation in §4.1, with a forward pointer at the end of the first paragraph of §2.4. Two reasons: (1) replayed movement is fixed and passengers are not represented, so other vehicles could not change any $M_R$ outcome; (2) in $M_A$ the competitors are what make charging costly. Add the like-for-like argument (cross-evaluation in $M_A$). This also answers #42, #49 and #53.
- **Proposed wording:**
  - End of §2.4, first paragraph (after "...in the model that can represent the outcomes of both."):
    New: "Only the agent-based model includes the ICE taxis that share the EVs' routes; Section~\ref{sec:methodology_design} explains why and how the designs are still compared like-for-like."
  - §4.1, first paragraph.
    Old (last sentence): "The electrified agents in \(\MA\) compete for passengers with synthetic ICE vehicles operating on the same corridors."
    New: "In \(\MA\), the EV agents compete for passengers with ICE competitors: synthetic agents that follow the same decision model and operate on the same routes (Section~\ref{sec:demand}). \(\MR\) has no ICE competitors, for two reasons. First, replayed movement is fixed and passengers are not represented, so other vehicles could not change any outcome of \(\MR\). Second, in \(\MA\) the competitors are what make charging costly: while an EV charges, they can carry the passengers that it would have carried. The designs are still compared like-for-like, because \(\xR\) and \(\xA\) are both evaluated in \(\MA\) against the same ICE competitors (Section~\ref{sec:sensitivity})."
- **Reply:** Section 2.4 now points ahead, and Section 4.1 explains the asymmetry. Competitors cannot affect replayed movement, and in the agent-based model they are what make charging cost passengers. Both designs are evaluated against the same competitors.

## #46 Table 1: "This study" row

- [x] Done
- **Where:** PDF p. 178, printed p. 154, Table 1 (`tab:related_work`). `main.tex:200`.
- **Comment:** "either bold this line, or put a midrule line above it. Or both"
- **Decision:** Add a `\midrule` above the row; keep normal weight.
- **Reply:** Done (rule above the row).

## #47, #48 Table 2: text too small

- [x] Done
- **Where:** PDF p. 180, printed p. 156, Table 2 (`tab:cpt_fleet_summary`). `main.tex:240-260`.
- **Comment (#47):** "This table text is way too small."
- **Comment (#48):** "either transpose table content, or make a landscape page dedicated to the table."
- **Cause:** `\resizebox{\textwidth}` shrinks a 10-column table, and more so at the thesis text width.
- **Decision:** Trim columns instead of transposing or rotating. Remove the Dates column (the dates are in the text at `main.tex:294`) and the Mean distance column (the two means that the text uses are stated in the study-days section). Remove `\resizebox` and set the table at `\footnotesize`.
- **Result:** Day class | Vehicles | Vehicle-days | Valid (%) | Long-dist. (%) | Distance (km), median [IQR] | Driving window (h), median [IQR] | Within range (%).
- **Fallback:** If it still overflows at the thesis width, break the [IQR] onto a second line in each cell (`\makecell`).
- **Reply:** I removed the dates (given in the text) and the mean distance and dropped the scaling, so the table is now at the normal table font size.

### Cross-cutting C: sync to the thesis and verify the layout

- [x] Build the paper (`main.tex`). There must be no undefined references or citations, apart from those of #58 until they are added.
- [ ] Re-sync `main.tex` and `appendix.tex` into `thesis/phd-thesis/replay_vs_abm/replay_vs_abm.tex`, as in thesis commit `8cc1b55` ("Updated the capstone chapter from source"). The round-2 diff does not apply as a patch (14 of 24 hunks fail), because the thesis copy strips comments, prefixes every label with `rva:` and keeps the appendices as "Appendix:" sections. The thesis copy also has uncommitted edits; a backup is in the session scratchpad (`replay_vs_abm.backup.tex`).
- [ ] Rebuild the thesis and check every Chapter 8 table at the thesis text width. Check especially Table 6 (`tab:models`), which has the same `X`-first-column layout as Table 20 (#57), plus Table 2 (#47) and Table 4 (#52, #53).
- [ ] Check the Chapter 8 entries in the List of Figures and List of Tables (one line each, no citations).

## #49 §4.1: ICE vehicles are also agents

- [x] Done
- **Where:** PDF p. 182, printed p. 158, §4.1, first paragraph. `main.tex:307`.
- **Marked:** "ICE vehicles operating on the same corridors."
- **Comment:** "which are also agent-based? Make that explicit"
- **Decision:** Yes. All drivers of a community share the same decision model (appendix, ODD "Heterogeneity"). Covered by the new §4.1 wording in #45 ("synthetic agents that follow the same decision model and operate on the same routes").
- **Reply:** Yes. They are agents with the same decision model as the EV agents, and Section 4.1 now says so.

## #50 §4.1: "electrify the same observed vehicles"

- [x] Done
- **Where:** PDF p. 182, printed p. 158, §4.1, second paragraph. `main.tex:309`. Also `main.tex:352` (Pipeline), `main.tex:358` (Figure 3 caption), §4.2.2 (`main.tex:373-376`) and the Table 6 caption (`main.tex:597`).
- **Marked:** "electrify the same observed vehicles"
- **Comment:** "does that mean you chose only N vehicles to electrify in both ABM case and replay case? I have a feeling not, which makes me wonder what you mean by this sentence."
- **Fact:** Both models electrify exactly the same vehicles: the qualified vehicles of each community (89 of 101 in Khayelitsha, 44 of 44 in Bellville, 20 of 26 in Wynberg). A vehicle qualifies when it keeps at least one eligible route after routes shorter than 5 km are excluded. The paper never defines "qualified", although Table 6 has a "Qualified Vehicles" column.
- **Proposed wording:**
  - §4.1.
    Old: "...and both electrify the same observed vehicles within each community."
    New: "...and both electrify the same vehicles in each community: its qualified vehicles, the observed vehicles that keep at least one eligible route of 5~km or more (Section~\ref{sec:routes})."
  - §4.2.2, add at the end: "A vehicle qualifies for the models when at least one of its eligible routes is 5~km or longer; 89 of the 101 vehicles qualify in Khayelitsha, all 44 in Bellville and 20 of the 26 in Wynberg (Table~\ref{tab:models})." (§4.2.2 is `sec:routes`, `main.tex:374`.)
  - Table 6 caption, add: "Qualified: the vehicles with an eligible route of 5~km or more, which both models electrify."
  - Pipeline (`main.tex:352`) and Figure 3 caption: "the same observed vehicles" → "the same qualified vehicles".
- **Reply:** Yes, exactly the same vehicles in both models: the qualified vehicles of each community (89, 44 and 20). The text now defines them and gives the numbers.

## #51 §4.1: "recorded dwell periods"

- [x] Done
- **Where:** PDF p. 182, printed p. 158, §4.1, second paragraph. `main.tex:309`.
- **Marked:** "[durin]g dwell"
- **Comment:** "during recorded dwell periods"
- **Proposed wording:** "...allows vehicles to charge during dwell periods..." → "...allows vehicles to charge during recorded dwell periods..."
- **Reply:** Done.

## #52 Table 4: "The agents of the community / The same agents"

- [x] Done
- **Where:** PDF p. 182, printed p. 158, Table 4 (`tab:model_comparison`), row "Electrified vehicles". `main.tex:320`.
- **Comment:** "Not clear."
- **Decision:** Apply Cross-cutting A and #50.
- **Proposed wording:**
  ```latex
  Electrified vehicles & The qualified vehicles of the community, replayed as observed EVs & The same vehicles, as EV agents & Same \\
  ```
- **Reply:** Rewritten. Both models electrify the community's qualified vehicles, which are replayed as observed EVs in $M_R$ and simulated as EV agents in $M_A$.

## #53 Table 4: "Other vehicles: None"

- [x] Done
- **Where:** PDF p. 182, printed p. 158, Table 4, row "Other vehicles". `main.tex:321`.
- **Comment:** "mmm I vaguely recall us discussing it, but now it makes no sense."
- **Decision:** State the reason in the row and point to the §4.1 paragraph (#45).
- **Proposed wording:**
  ```latex
  Other vehicles & None; replayed movement does not interact & ICE competitors: synthetic copies of the EV agents & \MA{} only \\
  ```
- **Reply:** This was our decision to leave competitors out of $M_R$, because they cannot affect replayed movement. The row and Section 4.1 now say so explicitly.

## #54 Table 5: praise

- **Where:** PDF p. 192, printed p. 168, Table 5 caption (`tab:objectives`).
- **Comment:** "Ah, OK, this is crucial. A lot now makes more sense."
- **Action:** None directly. The paper only became clear to him at Table 5, which supports moving the measures forward (#55).
- **Reply:** Thank you. This prompted moving the measures forward (see #55).

## #55 Table 5: move the measures before the method detail

- [x] Done
- **Where:** PDF p. 192, printed p. 168, Table 5. Now in §4.7.2 "Performance measures and selection rules", `main.tex:497-534`.
- **Comment:** "I wonder if the metrics should not precede some of the method detail. But TBH I am not sure."
- **Decision:** Move the measures into §4.1, as a new subsubsection "Model-native measures" right after "Planning principle" (`main.tex:345-348`).
- **Steps:**
  - [x] Move to §4.1: the opening paragraph of §4.7.2 ("Each model evaluates designs using the measures it can represent..."), Table 5, the paragraph defining the replay measures and the paired ICE counterfactual, the $\Delta_{\mathrm{EV}}$ and $\ell$ equation and the paragraph after it (`main.tex:499-534`).
  - [x] Merge or trim the second paragraph of "Planning principle" (`main.tex:348`), which already summarises the service measure of each model, so the two don't repeat each other.
  - [x] Rename §4.7.2 to "Selection rules". It keeps the replay front and TPE paragraphs (`main.tex:536-538`) and opens with a back-reference to the measures in §4.1.
  - [x] Labels: move `\label{sec:objectives}` with the measures and keep `\label{sec:selection}` on §4.7.2. Check every `\ref` to both (e.g. "The precise selection rules are given in Section~\ref{sec:objectives}" → `sec:selection`).
  - [x] The moved text uses terms that are defined later (evaluation days, TPE search, selection seeds). Add forward references, and rely on the role definitions in the caption (#56).
- **Reply:** Agreed. The model-native measures (Table 5 and their definitions) are now in Section 4.1, beside the planning principle, so the reader knows what each model optimises before reading the model details.

## #56 Table 5: "Front"

- [x] Done
- **Where:** PDF p. 192, printed p. 168, Table 5, $M_R$ column. `main.tex:512, 514`.
- **Comment:** "??"
- **Decision:** Change "Front" to "Pareto front" in the cells and define each role in the caption.
- **Proposed wording:**
  - Cells: "Front and selection" → "Pareto front and selection".
  - Add to the caption: "Role of each measure: Pareto front, an objective of the exact Pareto front of \MR{} over all designs; search, an objective of the TPE search of \MA; selection, used by the selection rule (Section~\ref{sec:selection}); reported, computed but not used to choose a design."
- **Reply:** The table now says "Pareto front", and the caption defines each role.

## #57 Table 20: text overlaps

- [x] Done
- **Where:** PDF p. 208, printed p. 184, Table 20 (`tab:computational_cost`). `main.tex:1021`.
- **Marked:** "Khayelitsha MR enumeration"
- **Comment:** "text overlaps"
- **Cause:** The first column (Community) is an `X` column in `@{}Xlrrrrr@{}`, which collapses at the thesis text width, so the Phase column overprints it.
- **Decision:** Make Community an `l` column and Phase the `X` column: `@{}lXrrrrr@{}`. Verify under Cross-cutting C.
- **Reply:** Fixed. The column widths are now set so the community and phase no longer overlap.

## #58 Appendix A: broken references

- [ ] Done (Joshua, later)
- **Where:** PDF p. 214, printed p. 190, Appendix A (community detection). `appendix.tex:11, 16, 23`.
- **Marked:** "ARI) [?] of its"
- **Comment:** "please check do for all broken references"
- **Cause:** Seven citation keys exist in no `.bib` file in the project: `salton1988_term_weighting`, `traag2019_louvain_to_leiden`, `newman2004_community_structure`, `reichardt2006_statistical_mechanics_communities`, `lancichinetti2012_consensus_clustering`, `hubert1985_comparing_partitions`, `strona2014_curveball`.
- **Owner:** Joshua will add the entries later.
- **Then:**
  - [ ] Rebuild the paper and check `main.log` for undefined citations and references.
  - [ ] Merge the entries into the thesis bibliography and repeat the check in the thesis build (Cross-cutting C).
- **Reply:** Fixed. The missing entries were added, and both the paper and the thesis build have no undefined references.

---

## Self-review (not from the supervisor)

After comments #41 to #57 were applied (commit `0af0e94`), a read-through of the paper found 20 further points of confusion. Joshua decided each one, and the project source (`embt_replay_vs_abm`: `docs/decisions.md`, `src/replay/`, `src/experiments/measures.py`, `experiments_fresh/*/main_means.parquet`) settled the factual ones. Every edit carries a `% CHANGE: ... (R2 self-review #N: ...)` comment. Line numbers refer to `main.tex` after these edits.

| # | Topic | Decision | Status |
|---|---|---|---|
| 1 | One-standard-error rule still cited in the Results | Remove it | [x] |
| 2 | "Viable" and "not stranded" both used for the $M_R$ measure | "Viable" only in the sense of Pretorius et al. | [x] |
| 3 | Below-reserve share defined two ways | Rename both; report the $M_A$ value | [x] |
| 4 | Two peak loads for the Khayelitsha $\mathbf{x}^\star_A$ | Tie each to its seed set | [x] |
| 5 | "Cost of $\mathbf{x}^\star_R$" changes sign and is defined late | Define it and its sign in §4.7.3 | [x] |
| 6 | "95% of the best design" vs the 99-connector ceiling | Ceiling = best enumerated design | [x] |
| 7 | 40 TPE trials vs 36 to 39 | Explain repeated proposals | [x] |
| 8 | Bound-check claim can't be checked | Name the design (19-8-6) | [x] |
| 9 | $M_A$ home energy 3 to 6 times that of $M_R$ | Explain from the source | [x] |
| 10 | "Qualif-" has four meanings | No change | n/a |
| 11 | "Validation" has four meanings | Clarify | [x] |
| 12 | V₃ name, "Binding" undefined, "gain" | Define binding and use it consistently | [x] |
| 13 | $k$ has three names | No change | n/a |
| 14 | ICE terms still mixed | "ICE competitors" in $M_A$ contexts | [x] |
| 15 | Smaller mismatches (associations, 140 km, conclusive, hold-back) | Fix each | [x] |
| 16 | TPE used in Table 5 before it is defined | Introduce it in §4.1.4 | [x] |
| 17 | Sensitivity ranges vs the rounded table | Check against unrounded values | [x] |
| 18 | Wynberg runs against the seed rationale | Reword | [x] |
| 19 | "No agent-based run strands" needs a scope | Limit to the base case | [x] |
| 20 | Capture shares above 1 unexplained | Explain | [x] |

### SR1 One-standard-error rule

- **Issue:** The Results cited a one-standard-error rule that round 1 removed from the Methods.
- **Change:** The sentence is removed from the RQ2 results (`main.tex:781`).

### SR2 "Viable"

- **Issue:** The Planning principle said $M_R$ selects on the share of days that "remain viable", while the rule used the not-stranded share. Below-reserve days are neither viable nor stranded.
- **Source:** Decision D142 and `src/replay/designs.py` (`OBJECTIVES = ("stranded_share", "peak_site_kw")`): $M_R$ selects on the steady-state not-stranded share.
- **Change:**
  - "Viable" is now used only as defined by Pretorius et al.: a vehicle-day that reaches a steady state without falling below the $0.2\,C$ reserve.
  - The Planning principle (`main.tex:366`) says $M_R$ selects on the not-stranded share, and why. Falling below the reserve is normal behaviour in $M_A$, so selecting on the viable share would not be like-for-like.
  - §4.3 (`main.tex:457`) defines viable, non-viable (below the reserve or stranded) and conclusive (not unconverged).
  - The "viable" ceiling of §5.1.3 became "not-stranded" (`main.tex:705`), and "make a pilot viable" became "for a pilot to succeed".

### SR3 Below-reserve share

- **Issue:** Table 5 said $M_A$ reports the below-reserve share under the same definition. The reference-design table said $M_A$ used another definition and left its cell empty.
- **Source:** `src/experiments/measures.py` (`below_reserve_share`). In $M_A$ it counts the agent-days on which a route run ends or a charging session starts below $0.2\,C$.
- **Change:**
  - Table 5 (`main.tex:372`) has two rows. "Non-viable share" ($M_R$): EV vehicle-days below $0.2\,C$ or stranded in the steady state. "Low-battery share" ($M_A$): EV agent-days with a route end or session start below $0.2\,C$.
  - A paragraph in §4.1.4 explains the difference.
  - The reference-design table (now Table 10, `main.tex:739`) reports both rows. The $M_A$ values for $\mathbf{x}^\star_R$ are 0.006, 0.004 and 0.016, from `experiments_fresh/*/main_means.parquet`.

### SR4 Khayelitsha peak load

- **Issue:** $\mathbf{x}^\star_A$ had a 600 kW peak in one place and 580 kW one paragraph later.
- **Change:** The text gives 600 kW on the ten fresh seeds and 580 kW on the selection seeds (`main.tex:781`).

### SR5 Cost of $\mathbf{x}^\star_R$

- **Issue:** The abstract and Results gave the cost as positive (11.9 points) and the tables as negative ($-0.119$), and only the Discussion defined it.
- **Change:**
  - §4.7.3 (`main.tex:594`) defines the cost as the points by which $\mathbf{x}^\star_R$ falls short of $\mathbf{x}^\star_A$. The tables report $\mathbf{x}^\star_R - \mathbf{x}^\star_A$, its negative.
  - The decomposition table's columns are renamed "Difference (SE)", and the text says that a negative part adds to the cost (`main.tex:912`).
  - The Discussion points back to the definition (`main.tex:1149`).

### SR6 Ceiling and selection wording

- **Issue:** The text called the 99-connector design the ceiling, but that design lies outside the design space. Table 4 and the sweep caption said "best design" and "cheapest design".
- **Source:** `src/replay/build.py` (`ceiling`) and `src/replay/designs.py` (`near_ceiling`). The ceiling is the highest not-stranded share of the enumerated designs. The 99-connector design only checks that the design space reaches it.
- **Change:**
  - §4.7.2 (`main.tex:577`) describes the ceiling and the check.
  - Table 4 (`main.tex:346`) now reads "At least 95% of the service of the best design, then the lowest peak site load and installed power".
  - The sweep caption (`main.tex:829`) says lowest peak, then lowest installed power. The fidelity table caption gives the ceiling over the design space.

### SR7 TPE trial count

- **Issue:** The Methods gave 40 trials; the Results and Table 20 gave 36 to 39.
- **Change:** §4.7.2 (`main.tex:577`) says that TPE proposes 40 trials. A repeated proposal reuses its first result, so the 40 trials evaluate 36 to 39 distinct designs.

### SR8 Bound check

- **Issue:** "The best validated Khayelitsha design reaches the bound at hubs 2 and 3" named no design, and neither design in the table reaches the bound.
- **Change:** The text names 19-8-6 (1,650 kW) and says why the bound matters (`main.tex:781`).

### SR9 Home energy

- **Issue:** $M_A$ reports 3 to 6 times the home energy of $M_R$, but the Limitations accounted for only 5 to 8 kWh more per vehicle-day.
- **Source:** `src/replay/build.py` (`replay_days`) and the study-folder aggregates.
- **Change:** §5.2 (`main.tex:739`) gives three reasons:
  - $M_R$ replays only the valid vehicle-days that are not long-distance days: about 58, 29 and 12 a day, against the 89, 44 and 20 EV agents of $M_A$.
  - A stranded vehicle leaves the active fleet and stops charging at home.
  - The simulated overnight periods of $M_A$ are 1.5 to 2.5 h longer.
- §4.3 (`main.tex:457`) states which days are replayed.

### SR10 "Qualif-"

- **Decision:** No change. Each use is qualified by its noun (vehicles, routes, communities, stop), and each definition is followed.

### SR11 Validation

- **Change:** A new opening paragraph in §4.5 (`main.tex:529`) separates calibration validation from a validated design and explains cold runs. "Validated design" is defined in §4.7.2 (`main.tex:577`).

### SR12 Binding

- **Issue:** V₃ was "depot only charging" in §4.2.3 but "hub charging only" in Table 6. "Binding" was never explained, and the Discussion called $V_2 - V_1$ "the gain".
- **Source:** `docs/communities.md`.
- **Change:**
  - §4.2.3 (`main.tex:449`): V₃ is hub charging only, without overnight charging. The binding of hub charging, $B = V_2 - V_1$, is the gain in the viable share. The rule reads "a binding of hub charging of at least 15 percentage points ($B \geq 15$)".
  - The Table 6 caption explains Binding (`main.tex:620`), and the Discussion uses the term.

### SR13 $k$

- **Decision:** No change. The three names refer to the same factor, and its definition covers every use.

### SR14 ICE terms

- **Change:** "ICE competitors" is used in the $M_A$ contexts: §2.4 (`main.tex:183`), §5.4, the Discussion (`main.tex:1176`) and the ODD Emergence paragraph (`appendix.tex:159`).

### SR15 Smaller mismatches

- **Change:**
  - "Route associations" → "taxi associations" (`main.tex:226`).
  - The 140 km range is removed from the introduction. It now reads "about 130 km for the battery window of the electric minibus of this study" (`main.tex:77`), which matches 0.7C × 70.47 / 0.38 = 129.8 km.
  - "Conclusive" is defined in §4.3 (`main.tex:457`).
  - Hold-back (drivers stop and wait for more passengers) is linked to the stop decision in §4.4.1 (`main.tex:482`).

### SR16 TPE before its definition

- **Change:** TPE is introduced in §4.1.4, with `\cite{watanabe2026_tpe}` (`main.tex:372`). §4.5 refers back to it (`main.tex:529`).

### SR17 Sensitivity ranges

- **Source:** `results/tables/synthesis/tab08_sensitivity.csv`. The unrounded values are: Bellville 2.63 to 3.94 and +0.12; Wynberg 5.90 to 15.07; the largest $k$ change 2.10. The text matches them.
- **Change:** The sensitivity table caption notes that the text uses unrounded values (`main.tex:1030`).

### SR18 Seed rationale

- **Issue:** The Methods said the selection seeds favour $\mathbf{x}^\star_A$, but in Wynberg the selection-seed difference (9.7) is smaller than the fresh-seed difference (10.3).
- **Change:** The sentence now says that the selection-seed differences are within one point of the fresh-seed values, in either direction (`main.tex:940`).

### SR19 "No run strands"

- **Issue:** Sensitivity runs strand on up to 0.37% of days.
- **Change:** The abstract (`main.tex:55`), the Results (`main.tex:739`) and the Discussion (`main.tex:1165`) limit the claim to the base case. Joshua had already changed Table 5's "Reported (must be 0)" to "Reported".

### SR20 Capture shares above 1

- **Change:** §4.7.3 (`main.tex:589`) and the ICE-capture caption (`main.tex:982`) explain that a share above 1 means the other drivers gained more passengers than the EVs lost. All such values are within two standard errors of 1.
