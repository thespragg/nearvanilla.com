from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_rails',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.*rail'])
    ))
