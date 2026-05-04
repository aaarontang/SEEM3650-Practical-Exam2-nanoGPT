# SEEM3650 Practical Exam 2 - nanoGPT Experiment

This repository contains my SEEM3650 Practical Exam 2 submission based on the open-source `karpathy/nanoGPT` repository.

## Project Summary

The practical exam includes:

1. Training a BabyGPT model on the Shakespeare character-level dataset.
2. Exploring model architecture settings by varying the number of attention heads.
3. Creating a code-generation dataset using open-source C/C++ code.
4. Training and sampling a character-level code-generation model.

## Student Information

Name: Aaron Tang Kwan Po  
Student ID: 1155192866  

## Important Files

- `report.md`  
  Main exam report containing generated samples, experiment results, and discussion.

- `config/train_shakespeare_char_exam.py`  
  Configuration file for the Shakespeare architecture exploration experiment.

- `plot_architecture_results.py`  
  Script used to generate the architecture comparison plot.

- `figures/shakespeare_heads_loss.png`  
  Plot comparing validation loss at iteration 5000.

- `data/code_generation/input.txt`  
  Open-source C/C++ code dataset used for the code-generation model.

- `config/train_code_generation.py`  
  Configuration file for the code-generation model.

## Architecture Experiment

Since `XYZ = 866` and `866 mod 4 = 2`, the number of layers was fixed at 7 and the number of attention heads was varied across:

```text
2, 3, 5, 7

The best validation loss at iteration 5000 was achieved by the 2-head model.

## Code-generation Dataset

Since 866 mod 2 = 0, open-source C/C++ code was used as the training dataset for the code-generation model.

## Attribution

This project is based on the original nanoGPT implementation by Andrej Karpathy:

https://github.com/karpathy/nanoGPT