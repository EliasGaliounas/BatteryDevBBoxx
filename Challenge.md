# Lithium-Ion Battery Field Data BBoxx Challenge

This document provides a general overview of the data sets, problems to tackle, and submission expectations for the field data challenge. For an overview of the more technical setup, expectations, and tools provided, see the [README](README.md)

## Data Description

The dataset consists of operational data of 200 lithium-ion battery systems. The data time-series data of voltage, current into, current out of, and temperature of the batteries. The sampling frequency of the temperature is lower. All quantities might contain NaN values. 

## Background

BBoxx operates off-grid Lithium-Ion Batteries in combination with solar panels in sub-Saharan Africa. The battery data is transferred over the air. Understanding how people use these batteries is essential for the development of future systems and also to understand battery degradation better. For the battery community, it is important that more operational data is shared publicly for testing and comparing their degradation models with real-world appliances.

## Challenge outline:

The core of this challenge is the characterization and clustering of usage
profiles. The usage of the devices plays an important role to understand how
the batteries age. Finding the number of groups is part of this challenge.
Whether you decide to use a feature-based approach or an approach that
works directly with the raw data is up to you. However, please keep in mind
that an excellent approach should allow being applied on many thousands of
devices with reasonable computational complexity. We encourage you to
explore creative approaches.
Based on these profiles come up with a method to generate new operational
profiles based on the dataset.
Part of the challenge is a visualization of the raw data and/or your approach
and/or your results.
We left some room for interpretation of this challenge to encourage different
approaches and pathways. In case you’re having questions or you’re getting
lost, please do join the office hours. This is a place where you can also chat
with people from other groups about questions and ideas you have in mind.

## Submission

Your submission for judging should be entirely contained within this repository. Please do not rename or repurpose the existing folders. If you decide to work with jupyter notebooks, please make sure all cells can be executed in the order of their appearance.

Please describe your approach and results in the [README](README.md) file. This can be text or simple bullet points. Please include your visualization as PDF file.

The repository upon submission should contain the MIT license, and not use any closed-source tools. Please replace the generic author text in [the license](LICENSE) with the names of your team members.

### Judging criteria:

This challenge will be judged by human judges based on different criteria.
Innovativeness of the approach
Interpretability of the approach
Creativity, understandability, and visual attractiveness of the visualization
Scalability of the algorithm to thousands of systems
Quality of the code and understandability
