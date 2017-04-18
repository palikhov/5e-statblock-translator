from spell_dict import spell_dict

common_dict = {
    "Armor Class ": "Класс Доспеха ",
    "Hit Points ": "Хиты ",
    "Speed ": "Скорость ",
    "ft.": "фт.",
    "Saving Throws ": "Спасброски ",
    "Special Senses ": "Чувства ",
    "fly": "полёт",
    "swim": "плавание",
    "burrow": "рытьё",
    "climb": "взбирание",
    "hover": "парение",
    "Senses ": "Чувства ",
    " darkvision ": " тёмное зрение ",
    "passive ": "пассивное ",
    "Condition Immunities": "Иммунитет к состояниям",
    "poisoned": "отравленный",
    "tremorsense": "чувство дрожи",
    "blindsight": "слепое зрение",
    "Challenge ": "Опасность ",
    " XP)": " опыта)",
    "": "",
    "": "",
    "": "",
    "": "",
    "Actions": "Действия",
    "ACTIONS": "Действия",
    "Multiattack.": "Мультиатака.",
    "one target": "одна цель",
    "Hit: ": "Попадание: ",
    "Magic Resistance. ": "Сопротивление магии. ",
    "Damage Immunities ": "Иммунитет к урону ",
    "Damage Resistances ": "Сопротивление к урону ",
    "Melee Weapon Attack:": "Рукопашная атака оружием:",
    "Melee Weapon attack:": "Рукопашная атака оружием:",
    " to hit, reach ": " к попаданию, досягаемость ",
    "Ranged Weapon Attack: ": "Дальнобойная атака оружием: ",
    "Ranged Weapon attack: ": "Дальнобойная атака оружием: ",
    " to hit, range": " к попаданию, дистанция",
    "(Recharge": "(Перезарядка",
    "Damage Vulnerabilities ": "Уязвимость к урону ",
    "Ranged Spell Attack:": "Дальнобойная атака заклинанием:",
    "Cantrip": "Заговор",
    "at will": "неограниченно",
    "telepathy": "телепатия",
    "understands": "понимает",
    "but can't speak": "но не может говорить",
# параметры
    "STR": "СИЛ",
    "DEX": "ЛОВ",
    "CON": "ТЕЛ",
    "INT": "ИНТ",
    "WIS": "МДР",
    "CHA": "ХАР",
    "Str ": "Сил ",
    "Dex ": "Лов ",
    "Con ": "Тел ",
    "Int ": "Инт ",
    "Wis ": "Мдр ",
    "Cha ": "Хар ",
}

damage_dict = {
# типы урона
    "damage": "урон",
    "plus": "плюс",
    "piercing": "колющий",
    "bludgeoning": "дробящий",
    "slashing": "рубящий",
    "fire": "огненный",
    "cold": "холод",
    "poison": "яд",
    "psychic": "психический",
    "acid": "кислотный",
    "lightning": "молния",
    "necrotic": "некротический",
}

alignment_dict = {
# мировоззрения
    "chaotic evil": "хаотично-злой",
    "lawful evil": "законно-злой",
    "neutral evil": "нейтрально-злой",
    "chaotic good": "хаотично-добрый",
    "lawful good": "законно-добрый",
    "neutral good": "нейтрально-добрый",
    "chaotic neutral": "хаотично-нейтральный",
    "lawful neutral": "законно-нейтральный",
    "neutral": "нейтральный",
    "unaligned": "без мировоззрения",
    "any non-good alignment": "любое не хорошее мировоззрение",
    "any good alignment": "любое хорошее мировоззрение",
}

armor_dict = {
    "shield": "щит",
    "scale armor": "чешуйчатый доспех",
    "scale mail": "чешуйчатый доспех",
    "": "",
    "natural armor": "естественный доспех",
    "with mage armor": "с магическим доспехом",
    "studded leather": "проклёпанный кожаный доспех",
    "Barkskin trait": "дубовая кора",
    "chain mail": "кольчуга",
    "chain shirt": "кольчужная рубаха",
    "ring mail": "колечный",
    "hide armor": "шкурный",
    "plate": "латы",
    "leather armor": "кожаный доспех",
}

creature_dict = {
# описания существ
    "Tiny": "Крошечный",
    "Small ": "Маленький ",
    "Medium": "Средний",
    "Large ": "Большой ",
    "Huge": "Огромный",
    "giant": "гигант",
    "humanoid": "гуманоид",
    "kobold": "кобольд",
    "fiend": "изверг",
    "monstrosity": "чудовище",
    "undead": "нежить",
    "goblinoid": "гоблиноид",
    "elemental": "элементаль",
    "beast": "зверь",
    "demon": "демон",
    "ooze": "слизь",
    "construct": "конструкция",
    "devil": "дьявол",
    "dragon": "дракон",
    "aberration": "аберрация",
    "plant": "растение",
    "fey": "фей",
}

weapon_dict = {
# weapon
    "Battleaxe": "Боевой топор",
    "Blowgun": "Духовая трубка",
    "Club": "Дубинка",
    "Crossbow, hand": "Арбалет, ручной",
    "Crossbow, heavy": "Арбалет, тяжёлый",
    "Crossbow, light": "Арбалет, лёгкий",
    "Dagger": "Кинжал",
    "Dart": "Дротик",
    "Flail": "Цеп",
    "Glaive": "Глефа",
    "Greataxe": "Секира",
    "Greatclub": "Палица",
    "Greatsword": "Двуручный меч",
    "Halberd": "Алебарда",
    "Handaxe": "Ручной топор",
    "Javelin": "Метательное копьё",
    "Lance": "Длинное копьё",
    "Light hammer": "Лёгкий молот",
    "Longbow": "Длинный лук",
    "Longsword": "Длинный меч",
    "Mace": "Булава",
    "Maul": "Молот",
    "Morningstar": "Моргенштерн",
    "Net": "Сеть",
    "Pike": "Пика",
    "Quarterstaff": "Боевой посох",
    "Rapier": "Рапира",
    "Scimitar": "Скимитар",
    "Shortbow": "Короткий лук",
    "Short Bow": "Короткий лук",
    "Shortsword": "Короткий меч",
    "Short Sword": "Короткий меч",
    "Sickle": "Серп",
    "Sling": "Праща",
    "Spear": "Копьё",
    "Trident": "Трезубец",
    "War pick": "Боевая кирка",
    "Warhammer": "Боевой молот",
    "Whip": "Кнут",    
    "Rock": "Камень",
    "Bite": "Укус",
    "Claw": "Когти",
}

lang_dict = {
    "Languages ": "Языки ",
    "Common": "Общий",
    "Elvish": "Эльфийский",
    "Dwarwish": "Дварфийский",
    "Giant": "Язык гигантов",
    "Ignan": "Игнан",
    "Bothii": "Ботхи",
    "Yikaria ": "Икария",
    "Draconic": "Драконий",
    "Goblin": "Гоблинский",
    "Orc": "Орочий",
    "Undercommon": "Подземный",
    "Telepathy": "Телепатия",
    "Abyssal": "Бездны",
}

condition_dict = {
    "": "",
    "Blinded": "Ослеплённый",
    "Charmed": "Очарованный",
    "Deafened": "Оглохший",
    "Frightened": "Испуганный",
    "Grappled": "Схваченный",
    "Incapacitated": "Недееспособный",
    "Invisible": "Невидимый",
    "Paralyzed": "Парализованный",
    "Petrified": "Окаменевший",
    "Poisoned": "Отравленный",
    "Prone": "Лежащий ничком",
    "Restrained": "Удерживаемый",
    "Stunned": "Ошеломлённый",
    "Unconscious": "Бессознательный",
}

skill_dict = {
    "": "",
    "Skills ": "Навыки ",
    "Acrobatics ": "Акробатика ",
    "Animal Handling ": "Уход за животными ",
    "Arcana ": "Магия ",
    "Athletics ": "Атлетика ",
    "Deception ": "Обман ",
    "History ": "История ",
    "Insight ": "Проницательность ",
    "Intimidation ": "Запугивание ",
    "Investigation ": "Расследование ",
    "Medicine ": "Медицина ",
    "Nature ": "Природа ",
    "Perception ": "Восприятие ",
    "Performance ": "Выступление ",
    "Persuasion ": "Убеждение ",
    "Religion ": "Религия ",
    "Sleight of Hand ": "Ловкость рук ",
    "Stealth ": "Скрытность ",
    "Survival ": "Выживание ",
}

item_dict = {**weapon_dict, **armor_dict}
all_dict = {**common_dict, **lang_dict, **skill_dict, **condition_dict, **item_dict,
    **alignment_dict, **creature_dict, **damage_dict}

