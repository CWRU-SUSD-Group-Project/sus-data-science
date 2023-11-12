#!/bin/bash

# Git
git config filter.strip-notebook-output-metadata.clean "python -m jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --ClearMetadataPreprocessor.preserve_nb_metadata_mask kernelspec --ClearMetadataPreprocessor.preserve_nb_metadata_mask name --to=notebook --stdin --stdout --log-level=ERROR"
git config filter.strip-notebook-output-metadata.smudge "cat"