from ideas.generator import Generator


def get_items():
    items = 'items'
    keys = [items]
    return Generator(context='Items', keys=keys)


def get_character():
    shape = 'shapes'
    nature = 'physical nature'
    characteristic = 'distinguishing characteristic'
    keys = [shape, nature, characteristic]
    return Generator(context='Character', keys=keys)


def get_env():
    season = 'season'
    time = 'time'
    inside = 'inside'
    outside = 'outside'
    keys = [season, time, inside, outside]
    return Generator(context='Environment', keys=keys)


def get_study():
    study = 'study'
    anatomy = 'anatomy'
    emotion = 'emotion'
    keys = [study, anatomy, emotion]
    return Generator(context='Study', keys=keys)


def get_exercise():
    exercise = 'exercise'
    keys = [exercise]
    return Generator(context='Exercise', keys=keys)
