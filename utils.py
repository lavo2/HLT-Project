
def get_ingredients(recipe: str, ner_result: list):
    ingredients = []
    last_added = 0
    b_word = 'B-FOOD'
    i_word = 'I-FOOD'

    for i in range(len(ner_result)):

        if ner_result[i]['entity'] == b_word:
            # check if previous word was a segmentation of the same one
            if ner_result[i]['word'].startswith('#') and ner_result[i-1]['entity'] == b_word:
                # if (for any reason (it happens)) the first word is a segment, we ignore it
                if last_added == 0:
                    continue
                ingredients[last_added-1] += recipe[ner_result[i]['start'] : ner_result[i]['end']]
            else:
                # get the ingredient from the recipe given its position
                ingredients.append(recipe[ner_result[i]['start'] : ner_result[i]['end']])
                last_added += 1

        elif ner_result[i]['entity'] == i_word:
            # check if segmentation is occurring
            if ner_result[i]['word'].startswith('#'):
                # if (for any reason (it happens)) the first word is a segment, we ignore it
                if last_added == 0:
                    continue
                ingredients[last_added-1] += recipe[ner_result[i]['start'] : ner_result[i]['end']]
            elif last_added == 0:
                ingredients.append(recipe[ner_result[i]['start'] : ner_result[i]['end']])
                last_added += 1
            else:
                ingredients[last_added-1] = ingredients[last_added-1] + ' ' + recipe[ner_result[i]['start'] : ner_result[i]['end']]

    return ingredients