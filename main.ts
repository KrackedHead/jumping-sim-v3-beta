namespace SpriteKind {
    export const HI = SpriteKind.create()
    export const OBJ = SpriteKind.create()
    export const Fire = SpriteKind.create()
}
controller.combos.attachCombo("uda", function () {
    Player.vy = -1500
    info.changeScoreBy(100)
    color.setPalette(
    color.Adafruit
    )
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Front`, function (sprite2, location2) {
    Cer_lev += 1
    Level()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Back`, function (sprite, location) {
    Cer_lev += -1
    Level()
})
info.onScore(1000, function () {
    Fireworks()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    trail += 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Player.vy == 0) {
        Player.vy = -150
    }
    info.changeScoreBy(1)
    if (trail == 0) {
        Player.startEffect(effects.warmRadial, 1000)
    } else if (trail <= 1) {
        Player.startEffect(effects.warmRadial, 0)
    }
})
controller.combos.attachCombo("uuddlrlrab", function () {
    if (Player.vy == 0) {
        Player.vy = 150
    }
    info.setScore(0)
    color.setPalette(
    color.originalPalette
    )
    game.splash("loser")
})
function Level () {
    if (Cer_lev == 0) {
        tiles.setCurrentTilemap(tilemap`level2`)
        scene.setBackgroundImage(assets.image`SPPPPPPPPPPPPPPPPPPPPPPPPPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE`)
    } else if (Cer_lev == 1) {
        tiles.setCurrentTilemap(tilemap`Holloween`)
        scene.setBackgroundImage(assets.image`Holloween`)
    } else if (Cer_lev == 2) {
        tiles.setCurrentTilemap(tilemap`level4`)
        scene.setBackgroundImage(assets.image`Aquatic`)
    } else if (Cer_lev == 3) {
        tiles.setCurrentTilemap(tilemap`level5`)
        scene.setBackgroundImage(assets.image`myImage`)
    }
    tiles.placeOnRandomTile(Player, assets.tile`Spawn`)
    for (let value of tiles.getTilesByType(assets.tile`Spawn`)) {
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
}
function Fireworks () {
    value.startEffect(effects.spray, 5000)
    pause(2000)
    value.startEffect(effects.trail, 5000)
    pause(2000)
    value.startEffect(effects.fountain, 5000)
    pause(2000)
    value.startEffect(effects.confetti, 5000)
    pause(2000)
    value.startEffect(effects.hearts, 5000)
    pause(2000)
    value.startEffect(effects.smiles, 5000)
    pause(2000)
    value.startEffect(effects.rings, 5000)
    pause(2000)
    value.startEffect(effects.fire, 5000)
    pause(2000)
    value.startEffect(effects.warmRadial, 5000)
    pause(2000)
    value.startEffect(effects.coolRadial, 5000)
    pause(2000)
    value.startEffect(effects.halo, 5000)
    pause(2000)
    value.startEffect(effects.ashes, 5000)
    pause(2000)
    value.startEffect(effects.disintegrate, 5000)
    pause(2000)
    value.startEffect(effects.blizzard, 5000)
    pause(2000)
    value.startEffect(effects.bubbles, 5000)
    pause(2000)
    value.startEffect(effects.starField, 5000)
}
let trail = 0
let value: Sprite = null
let Player: Sprite = null
let Cer_lev = 0
Cer_lev = 0
game.splash("Objective: Jump", "Only use keyboard")
info.setScore(0)
controller.moveSprite(Player, 80, 0)
Player = sprites.create(assets.image`Player`, SpriteKind.Player)
let value2 = sprites.create(assets.image`HI`, SpriteKind.HI)
value2.setPosition(60, 90)
value = sprites.create(assets.image`Fireworks`, SpriteKind.Fire)
value.setPosition(120, 115)
scene.cameraFollowSprite(Player)
Level()
controller.moveSprite(Player, 80, 0)
trail = 0
game.onUpdate(function () {
    if (Player.vy < 0) {
        Player.setImage(assets.image`UP`)
    } else if (Player.x % 2 == 0) {
        Player.setImage(assets.image`Player`)
    }
    if ((Player.isHittingTile(CollisionDirection.Left) || Player.isHittingTile(CollisionDirection.Right)) && Player.vy >= 0) {
        Player.vx = 0
        Player.ay = 0
        Player.setImage(assets.image`Player`)
    } else {
        Player.ay = 350
    }
})
