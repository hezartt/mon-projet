#' Calculer l'indice de masse corporelle (BMI)
#'
#' @param weight_kg Poids en kilogrammes (numérique)
#' @param height_m Taille en mètres (numérique)
#'
#' @return L'indice de masse corporelle (numérique)
#' @export
#'
#' @examples
#' calculate_bmi(70, 1.75)
calculate_bmi <- function(weight_kg, height_m) {
  if (weight_kg <= 0 || height_m <= 0) {
    stop("Le poids et la taille doivent être positifs")
  }
  weight_kg / (height_m ^ 2)
}

#' Catégoriser le BMI
#'
#' @param bmi L'indice de masse corporelle (numérique)
#'
#' @return La catégorie : 'Insuffisant', 'Normal', 'Surpoids', 'Obésité' (character)
#' @export
#'
#' @examples
#' categorize_bmi(22)
categorize_bmi <- function(bmi) {
  if (bmi < 18.5) {
    return("Insuffisant")
  } else if (bmi < 25) {
    return("Normal")
  } else if (bmi < 30) {
    return("Surpoids")
  } else {
    return("Obésité")
  }
}

#' Créer un patient
#'
#' @param name Nom du patient
#' @param weight_kg Poids en kg
#' @param height_m Taille en m
#' @param age Âge en années
#'
#' @return Une liste contenant les infos du patient
#' @export
#'
#' @examples
#' patient <- create_patient("Jean Dupont", 70, 1.75, 45)
create_patient <- function(name, weight_kg, height_m, age) {
  if (age < 0 || age > 150) {
    stop("L'âge doit être entre 0 et 150")
  }

  list(
    name = name,
    weight_kg = weight_kg,
    height_m = height_m,
    age = age,
    bmi = calculate_bmi(weight_kg, height_m)
  )
}