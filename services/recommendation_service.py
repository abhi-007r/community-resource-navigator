def extract_categories(
    situation: str
):
    text = situation.lower()

    categories = []

    if any(
        word in text
        for word in [
            "food",
            "hungry",
            "groceries"
        ]
    ):
        categories.append("Food")

    if any(
        word in text
        for word in [
            "job",
            "employment",
            "work"
        ]
    ):
        categories.append(
            "Workforce Development"
        )

    if any(
        word in text
        for word in [
            "housing",
            "rent",
            "homeless"
        ]
    ):
        categories.append("Housing")

    if any(
        word in text
        for word in [
            "mental",
            "anxiety",
            "depression"
        ]
    ):
        categories.append(
            "Mental Health"
        )

    return categories


def extract_categories_ai_ready(
    situation: str
):
    """
    Placeholder for future Claude integration.
    """

    return extract_categories(
        situation
    )