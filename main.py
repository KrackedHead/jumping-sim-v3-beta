@namespace
class SpriteKind:
    HI = SpriteKind.create()
    OBJ = SpriteKind.create()
    Fire = SpriteKind.create()

def on_combos_attach_combo():
    Player.vy = -1500
    info.change_score_by(100)
    color.set_palette(color.adafruit)
controller.combos.attach_combo("uda", on_combos_attach_combo)

def on_overlap_tile(sprite2, location2):
    global Cer_lev
    Cer_lev += 1
    Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Front
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    global Cer_lev
    Cer_lev += -1
    Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Back
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global trail
    trail += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile3)

def on_a_pressed():
    if Player.vy == 0:
        Player.vy = -150
    info.change_score_by(1)
    if trail == 0:
        Player.start_effect(effects.warm_radial, 1000)
    elif trail <= 1:
        Player.start_effect(effects.warm_radial, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_combos_attach_combo2():
    if Player.vy == 0:
        Player.vy = 150
    info.set_score(0)
    color.set_palette(color.original_palette)
    game.splash("loser")
controller.combos.attach_combo("uuddlrlrab", on_combos_attach_combo2)

def on_on_score():
    Fireworks()
info.on_score(100, on_on_score)

def Level():
    if Cer_lev == 0:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        scene.set_background_image(assets.image("""
            SPPPPPPPPPPPPPPPPPPPPPPPPPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        """))
    elif Cer_lev == 1:
        tiles.set_current_tilemap(tilemap("""
            Holloween
        """))
        scene.set_background_image(assets.image("""
            Holloween
        """))
    elif Cer_lev == 2:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        scene.set_background_image(assets.image("""
            Aquatic
        """))
    elif Cer_lev == 3:
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        scene.set_background_image(assets.image("""
            myImage
        """))
    tiles.place_on_random_tile(Player, assets.tile("""
        Spawn
    """))
    for value in tiles.get_tiles_by_type(assets.tile("""
        Spawn
    """)):
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
def Fireworks():
    value2.start_effect(effects.spray, 5000)
    pause(2000)
    value2.start_effect(effects.trail, 5000)
    pause(2000)
    value2.start_effect(effects.fountain, 5000)
    pause(2000)
    value2.start_effect(effects.confetti, 5000)
    pause(2000)
    value2.start_effect(effects.hearts, 5000)
    pause(2000)
    value2.start_effect(effects.smiles, 5000)
    pause(2000)
    value2.start_effect(effects.rings, 5000)
    pause(2000)
    value2.start_effect(effects.fire, 5000)
    pause(2000)
    value2.start_effect(effects.warm_radial, 5000)
    pause(2000)
    value2.start_effect(effects.cool_radial, 5000)
    pause(2000)
    value2.start_effect(effects.halo, 5000)
    pause(2000)
    value2.start_effect(effects.ashes, 5000)
    pause(2000)
    value2.start_effect(effects.disintegrate, 5000)
    pause(2000)
    value2.start_effect(effects.blizzard, 5000)
    pause(2000)
    value2.start_effect(effects.bubbles, 5000)
    pause(2000)
    value2.start_effect(effects.star_field, 5000)
    pause(2000)
    value2.start_effect(effects.clouds, 5000)
trail = 0
value2: Sprite = None
Player: Sprite = None
Cer_lev = 0
Cer_lev = 0
game.splash("Objective: Jump", "Only use keyboard")
info.set_score(0)
controller.move_sprite(Player, 80, 0)
Player = sprites.create(assets.image("""
    Player
"""), SpriteKind.player)
value22 = sprites.create(assets.image("""
    HI
"""), SpriteKind.HI)
value22.set_position(60, 90)
value2 = sprites.create(assets.image("""
    Fireworks
"""), SpriteKind.Fire)
value2.set_position(120, 115)
scene.camera_follow_sprite(Player)
Level()
controller.move_sprite(Player, 80, 0)
trail = 0

def on_on_update():
    if Player.vy < 0:
        Player.set_image(assets.image("""
            UP
        """))
    elif Player.x % 2 == 0:
        Player.set_image(assets.image("""
            Player
        """))
    if (Player.is_hitting_tile(CollisionDirection.LEFT) or Player.is_hitting_tile(CollisionDirection.RIGHT)) and Player.vy >= 0:
        Player.vx = 0
        Player.ay = 0
        Player.set_image(assets.image("""
            UP0
        """))
    else:
        Player.ay = 350
game.on_update(on_on_update)
