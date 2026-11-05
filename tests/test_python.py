"""Tests pour le module de santé"""

import pytest
from src.health_module import calculate_bmi, categorize_bmi, Patient


class TestCalculateBMI:
    """Tests pour calculate_bmi"""

    def test_normal_calculation(self):
        """Tester un calcul normal"""
        assert calculate_bmi(70, 1.75) == pytest.approx(22.86, abs=0.01)

    def test_underweight(self):
        """Tester un poids insuffisant"""
        assert calculate_bmi(50, 1.75) == pytest.approx(16.33, abs=0.01)

    def test_invalid_weight(self):
        """Tester avec poids négatif"""
        with pytest.raises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_zero_height(self):
        """Tester avec taille zéro"""
        with pytest.raises(ValueError):
            calculate_bmi(70, 0)


class TestCategorizeBMI:
    """Tests pour categorize_bmi"""

    def test_insufficient_bmi(self):
        """Tester catégorie insuffisante"""
        assert categorize_bmi(18.0) == "Insuffisant"

    def test_normal_bmi(self):
        """Tester catégorie normale"""
        assert categorize_bmi(22.0) == "Normal"

    def test_overweight_bmi(self):
        """Tester catégorie surpoids"""
        assert categorize_bmi(27.0) == "Surpoids"

    def test_obese_bmi(self):
        """Tester catégorie obésité"""
        assert categorize_bmi(32.0) == "Obésité"


class TestPatient:
    """Tests pour la classe Patient"""

    def test_patient_creation(self):
        """Tester la création d'un patient"""
        patient = Patient("Jean Dupont", 70, 1.75, 45)
        assert patient.name == "Jean Dupont"
        assert patient.age == 45

    def test_patient_invalid_age(self):
        """Tester avec un âge invalide"""
        with pytest.raises(ValueError):
            Patient("Jean", 70, 1.75, 200)

    def test_patient_bmi_calculation(self):
        """Tester le calcul du BMI pour un patient"""
        patient = Patient("Jean", 70, 1.75, 45)
        assert patient.get_bmi() == pytest.approx(22.86, abs=0.01)

    def test_patient_representation(self):
        """Tester la représentation du patient"""
        patient = Patient("Jean", 70, 1.75, 45)
        assert "Jean" in repr(patient)
        assert "45" in repr(patient)