# Changelog — D&D 2024 Character JSON spec

This spec follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (e.g. 1.x → 2.0.0): breaking changes to field names/shapes. A parser
  written for 1.x may not read a 2.x document.
- **MINOR** (1.0 → 1.1): new optional fields, additive only. 1.x parsers keep working.
- **PATCH** (1.0.0 → 1.0.1): clarifications, docs, constraint fixes — no shape change.

A document declares the version it targets via the top-level `spec_version` field.
Tools should accept any document whose MAJOR matches and whose MINOR is ≤ the
version they implement.

## 1.0.0 — 2026-06-15

Initial release.

- Top-level identity: `name`, `player`, `species` (object with `lineage` +
  structured `traits`), `classes` (array, multiclass-ready), `background`,
  `alignment`, `xp`.
- `abilities`, `saving_throws`, `skills` (proficient/expertise), `skill_bonuses`
  (flat feat/item bonuses).
- Combat: `armor_class`, `shield`, `initiative`, `speed` (walk/fly/climb/…),
  `size`, `senses`, `passive_perception`, `hit_points`, `hit_dice`, `death_saves`.
- `proficiencies` (armor/weapons/tools/languages), `weapons`, `feats`,
  `class_features`, `equipment`, `coins`, `attunement`.
- `spellcasting` (DC/attack derived from ability), `spell_slots`, `spells`.
- Designed for D&D 2024 (5.5e): species terminology, expertise, feat-granting
  backgrounds, and homebrew species/feats are all first-class.
