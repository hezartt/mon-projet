"""
Module pour l'analyse de données de santé
"""

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculer l'indice de masse corporelle (BMI)

    Args:
        weight_kg: Poids en kilogrammes
        height_m: Taille en mètres

    Returns:
        L'indice de masse corporelle

    Raises:
        ValueError: Si les paramètres sont invalides
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Le poids et la taille doivent être positifs")

    return weight_kg / (height_m ** 2)


def categorize_bmi(bmi: float) -> str:
    """
    Catégoriser le BMI

    Args:
        bmi: L'indice de masse corporelle

    Returns:
        La catégorie: 'Insuffisant', 'Normal', 'Surpoids', 'Obésité'
    """
    if bmi < 18.5:
        return "Insuffisant"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Surpoids"
    else:
        return "Obésité"


class Patient:
    """Représenter un patient"""

    def __init__(self, name: str, weight_kg: float, height_m: float, age: int):
        """
        Initialiser un patient

        Args:
            name: Nom du patient
            weight_kg: Poids en kg
            height_m: Taille en m
            age: Âge en années
        """
        if age < 0 or age > 150:
            raise ValueError("L'âge doit être entre 0 et 150")

        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.age = age

    def get_bmi(self) -> float:
        """Retourner le BMI du patient"""
        return calculate_bmi(self.weight_kg, self.height_m)

    def get_bmi_category(self) -> str:
        """Retourner la catégorie de BMI"""
        return categorize_bmi(self.get_bmi())

    def __repr__(self) -> str:
        return f"Patient({self.name}, {self.age} ans, BMI={self.get_bmi():.1f})"