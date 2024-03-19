from json import dumps

articles = [
    {
        "id": 1,
        "name": "Ноутбук",
        "main_shelf": "А",
        "opt_shelfs": dumps([])
    },
    {
        "id": 2,
        "name": "Телевизор",
        "main_shelf": "А",
        "opt_shelfs": dumps([])
    },
    {
        "id": 3,
        "name": "Телефон",
        "main_shelf": "Б",
        "opt_shelfs": dumps(["З", "В"])
    },
    {
        "id": 4,
        "name": "Системный блок",
        "main_shelf": "Ж",
        "opt_shelfs": dumps([])
    },
    {
        "id": 5,
        "name": "Часы",
        "main_shelf": "Ж",
        "opt_shelfs": dumps(["А"])
    },
    {
        "id": 6,
        "name": "Микрофон",
        "main_shelf": "Ж",
        "opt_shelfs": dumps([])
    },
]

orders = [
    {
        "id": 10,
        "articles": dumps([
            {
                "id": 1,
                "amount": 2
            },
            {
                "id": 3,
                "amount": 1
            },
            {
                "id": 6,
                "amount": 1
            },

        ])
    },
    {
        "id": 11,
        "articles": dumps(
            [
                {
                    "id": 2,
                    "amount": 3
                },

            ]
        )
    },
    {
        "id": 14,
        "articles": dumps([
            {
                "id": 1,
                "amount": 3
            },
            {
                "id": 4,
                "amount": 4
            },

        ])
    },
    {
        "id": 15,
        "articles": dumps([
            {
                "id": 5,
                "amount": 1
            },

        ])
    },

]
