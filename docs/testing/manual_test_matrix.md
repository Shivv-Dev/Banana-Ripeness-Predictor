# Manual Test Matrix

## Overview

This document defines the manual testing strategy for Banalyzer, a production-inspired banana ripeness classification application.

The objective is to verify that the application behaves correctly under normal, invalid, and edge-case conditions while providing a stable and user-friendly experience.

The testing process covers:

- Functional testing
- Negative testing
- Edge-case testing
- UI validation
- Performance validation

Each test case includes a unique identifier, expected behavior, observed behavior, and execution status.

---

## Test Environment

| Item | Value |
|------|-------|
| Application | Banalyzer |
| Python | 3.13 |
| Framework | Streamlit |
| ML Framework | TensorFlow 2.20 |
| Model | MobileNetV2 Transfer Learning |
| Operating System | Windows |
| Testing Type | Manual Functional Testing |

---

## Test Status Legend

| Status | Meaning |
|---------|---------|
| ✅ Pass | Test completed successfully |
| ❌ Fail | Expected behavior not achieved |
| ⚠ Not Tested | Test has not yet been executed |

---

# Functional Test Cases

## Application Startup

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-001 | Launch the application | Application starts without errors | | ⚠ Not Tested |
| TC-002 | Verify page configuration | Correct page title and favicon are displayed | | ⚠ Not Tested |
| TC-003 | Verify sidebar rendering | Sidebar is displayed correctly | | ⚠ Not Tested |
| TC-004 | Verify header rendering | Header section is displayed correctly | | ⚠ Not Tested |

---

## Image Upload

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-005 | Upload a valid JPG image | Image preview is displayed successfully | | ⚠ Not Tested |
| TC-006 | Upload a valid PNG image | Image preview is displayed successfully | | ⚠ Not Tested |

---

## Prediction Pipeline

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-007 | Predict ripeness from a valid banana image | Prediction is generated successfully | | ⚠ Not Tested |
| TC-008 | Display confidence badge | Confidence badge is shown with the correct label and color | | ⚠ Not Tested |
| TC-009 | Display confidence gauge | Confidence gauge reflects the prediction confidence | | ⚠ Not Tested |
| TC-010 | Display probability distribution | Probability chart displays all class probabilities | | ⚠ Not Tested |
| TC-011 | Display prediction explanation | Explanation matches the predicted ripeness class | | ⚠ Not Tested |
| TC-012 | Display runner-up prediction | Second-highest prediction is shown correctly | | ⚠ Not Tested |

---

## Prediction Details

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-013 | Display ripeness insights | Insight card matches predicted class | | ⚠ Not Tested |
| TC-014 | Display prediction metadata | Prediction metadata is displayed correctly | | ⚠ Not Tested |
| TC-015 | Display banana lifecycle | Current lifecycle stage is highlighted correctly | | ⚠ Not Tested |
| TC-016 | Display model information | Model information dashboard renders correctly | | ⚠ Not Tested |

---

## Application Stability

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-017 | Generate multiple consecutive predictions | Application remains stable without crashes | | ⚠ Not Tested |
| TC-018 | Verify temporary file cleanup | Temporary files are deleted after prediction | | ⚠ Not Tested |
| TC-019 | Verify logging | Successful prediction is recorded in the application logs | | ⚠ Not Tested |

---

# Negative Test Cases

## Invalid File Handling

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-020 | Upload a PDF file | Unsupported file type is rejected without crashing | | ⚠ Not Tested |
| TC-021 | Upload a TXT file | Unsupported file type is rejected without crashing | | ⚠ Not Tested |
| TC-022 | Upload a corrupted image | Friendly error message is displayed | | ⚠ Not Tested |

---

## Prediction Failures

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-023 | Prediction model cannot be loaded | Friendly error message is displayed and the application remains responsive | | ⚠ Not Tested |
| TC-024 | Invalid prediction index returned | Prediction validation detects the issue and prevents incorrect output | | ⚠ Not Tested |
| TC-025 | Invalid probability distribution returned | Prediction validation reports an error instead of displaying invalid results | | ⚠ Not Tested |
| TC-026 | Unexpected exception during inference | Exception is logged and the application remains stable | | ⚠ Not Tested |

---

## Resource Management

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-027 | Prediction fails after temporary file creation | Temporary file is removed during cleanup | | ⚠ Not Tested |
| TC-028 | Multiple failed predictions | Application remains responsive without requiring a restart | | ⚠ Not Tested |

---

## Logging

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-029 | Exception occurs during prediction | Error is recorded in the application log | | ⚠ Not Tested |
| TC-030 | Validation failure occurs | Validation error is recorded in the application log | | ⚠ Not Tested |

---

# Edge Case Test Cases

## Challenging Image Conditions

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-031 | Upload a very dark banana image | Prediction completes without application failure | | ⚠ Not Tested |
| TC-032 | Upload an overexposed banana image | Prediction completes without application failure | | ⚠ Not Tested |
| TC-033 | Upload a blurry banana image | Prediction completes and confidence score is displayed | | ⚠ Not Tested |
| TC-034 | Upload a rotated banana image | Prediction completes successfully | | ⚠ Not Tested |
| TC-035 | Upload a high-resolution image | Image is resized automatically and prediction succeeds | | ⚠ Not Tested |
| TC-036 | Upload a very small image | Prediction completes successfully | | ⚠ Not Tested |

---

## Complex Scene Images

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-037 | Upload an image containing multiple bananas | Prediction completes without crashing | | ⚠ Not Tested |
| TC-038 | Upload an image where the banana occupies only a small portion of the frame | Prediction completes successfully | | ⚠ Not Tested |
| TC-039 | Upload a partially occluded banana | Prediction completes successfully | | ⚠ Not Tested |
| TC-040 | Upload an image with a cluttered background | Prediction completes successfully | | ⚠ Not Tested |

---

## Out-of-Distribution Inputs

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-041 | Upload an image with no banana present | Prediction completes without crashing and confidence is displayed | | ⚠ Not Tested |
| TC-042 | Upload an image of another fruit | Prediction completes without crashing | | ⚠ Not Tested |
| TC-043 | Upload a grayscale banana image | Prediction completes successfully | | ⚠ Not Tested |
| TC-044 | Upload a screenshot of a banana image | Prediction completes successfully | | ⚠ Not Tested |

---

## Continuous Usage

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-045 | Perform 20 consecutive predictions | Application remains stable throughout testing | | ⚠ Not Tested |
| TC-046 | Alternate between valid and invalid uploads | Application continues operating correctly | | ⚠ Not Tested |

---

# UI Validation Test Cases

## Prediction Dashboard

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-047 | Verify prediction summary | Predicted class, confidence score, and confidence badge are displayed correctly | | ⚠ Not Tested |
| TC-048 | Verify confidence badge | Badge label, color, and icon match the confidence level | | ⚠ Not Tested |
| TC-049 | Verify confidence gauge | Gauge percentage matches the reported confidence score | | ⚠ Not Tested |
| TC-050 | Verify probability distribution | All output classes are displayed with valid probability values | | ⚠ Not Tested |
| TC-051 | Verify runner-up prediction | Second-highest prediction is displayed correctly | | ⚠ Not Tested |

---

## Information Panels

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-052 | Verify prediction explanation | Explanation corresponds to the predicted ripeness class | | ⚠ Not Tested |
| TC-053 | Verify ripeness insights | Insights match the predicted class metadata | | ⚠ Not Tested |
| TC-054 | Verify prediction metadata | Architecture, input resolution, inference time, and top prediction are displayed correctly | | ⚠ Not Tested |
| TC-055 | Verify banana lifecycle visualization | Current ripeness stage is highlighted correctly | | ⚠ Not Tested |
| TC-056 | Verify model information dashboard | Model architecture, framework, accuracy, output classes, input resolution, and inference device are displayed correctly | | ⚠ Not Tested |

---

## Layout Consistency

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-057 | Verify sidebar layout | Sidebar renders correctly without overlap or missing elements | | ⚠ Not Tested |
| TC-058 | Verify header layout | Header content is displayed correctly | | ⚠ Not Tested |
| TC-059 | Verify footer layout | Footer renders correctly | | ⚠ Not Tested |
| TC-060 | Verify dashboard responsiveness | Dashboard remains readable after multiple predictions | | ⚠ Not Tested |

---

# Performance Validation Test Cases

## Prediction Performance

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-061 | Execute the first prediction after application startup | Prediction completes successfully and inference time is displayed | | ⚠ Not Tested |
| TC-062 | Execute multiple consecutive predictions | Predictions complete successfully without application instability | | ⚠ Not Tested |
| TC-063 | Compare inference times across repeated predictions | Inference times remain reasonably consistent under similar conditions | | ⚠ Not Tested |

---

## Application Responsiveness

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-064 | Upload several images sequentially | Application remains responsive throughout testing | | ⚠ Not Tested |
| TC-065 | Perform repeated predictions without refreshing the page | No noticeable UI degradation or freezing occurs | | ⚠ Not Tested |
| TC-066 | Verify dashboard rendering after prediction | Prediction results are displayed without rendering errors | | ⚠ Not Tested |

---

## Resource Stability

| ID | Test Scenario | Expected Result | Actual Result | Status |
|----|---------------|-----------------|---------------|--------|
| TC-067 | Execute extended prediction session | Application continues operating without crashes | | ⚠ Not Tested |
| TC-068 | Verify temporary file cleanup after repeated predictions | No orphaned temporary files remain after testing | | ⚠ Not Tested |
| TC-069 | Verify application logging during extended usage | Prediction events and errors are consistently recorded in the log | | ⚠ Not Tested |

---

# Manual Validation Checklist

Complete this checklist before creating a release, recording a demo, or publishing updates.

## Application Startup

- [ ] Application launches successfully.
- [ ] No exceptions are displayed during startup.
- [ ] Page title and favicon are correct.
- [ ] Sidebar renders correctly.
- [ ] Header renders correctly.

---

## Image Upload

- [ ] Valid JPG images upload successfully.
- [ ] Valid PNG images upload successfully.
- [ ] Uploaded image preview is displayed correctly.

---

## Prediction Pipeline

- [ ] Prediction completes successfully.
- [ ] Predicted ripeness class is displayed.
- [ ] Confidence score is displayed.
- [ ] Confidence badge is correct.
- [ ] Confidence gauge matches the confidence score.
- [ ] Probability distribution displays all output classes.
- [ ] Runner-up prediction is displayed.

---

## Prediction Details

- [ ] Prediction explanation matches the predicted class.
- [ ] Ripeness insights are displayed correctly.
- [ ] Prediction metadata is accurate.
- [ ] Banana lifecycle visualization is correct.
- [ ] Model information dashboard is displayed correctly.

---

## Error Handling

- [ ] Invalid files are handled gracefully.
- [ ] Friendly error messages are displayed.
- [ ] Application remains stable after prediction failures.
- [ ] Exceptions are written to the log.

---

## Resource Management

- [ ] Temporary files are cleaned up.
- [ ] Multiple predictions execute successfully.
- [ ] Application remains responsive throughout testing.

---

## Final Review

- [ ] No visual layout issues observed.
- [ ] No unexpected application crashes.
- [ ] Logging is functioning correctly.
- [ ] Testing documentation has been updated.
- [ ] Application is ready for demonstration or release.

---