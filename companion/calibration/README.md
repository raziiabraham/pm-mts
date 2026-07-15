# Chapter 14: filled calibration record

`filled_record.json` carries the constructed `domain` failure from Chapter 13 through diagnosis, a bounded resolver change, regression comparison, release decision, and remaining limits.

Run:

```sh
python3 companion/calibration/validate_record.py
```

The validator cross-checks the record against the actual Chapter 13 dataset and version outputs. This prevents a calibration narrative from drifting away from its preserved case.
