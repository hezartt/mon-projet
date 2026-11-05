library(testthat)

# Source les fonctions
source("src/health_functions.R")

test_that("calculate_bmi works correctly", {
  bmi <- calculate_bmi(70, 1.75)
  expect_equal(bmi, 22.86, tolerance = 0.01)
})

test_that("calculate_bmi rejects invalid inputs", {
  expect_error(calculate_bmi(-70, 1.75))
  expect_error(calculate_bmi(70, 0))
})

test_that("categorize_bmi works correctly", {
  expect_equal(categorize_bmi(18.0), "Insuffisant")
  expect_equal(categorize_bmi(22.0), "Normal")
  expect_equal(categorize_bmi(27.0), "Surpoids")
  expect_equal(categorize_bmi(32.0), "Obésité")
})

test_that("create_patient works correctly", {
  patient <- create_patient("Jean", 70, 1.75, 45)
  expect_equal(patient$name, "Jean")
  expect_equal(patient$age, 45)
  expect_equal(patient$bmi, 22.86, tolerance = 0.01)
})

test_that("create_patient rejects invalid ages", {
  expect_error(create_patient("Jean", 70, 1.75, 200))
})