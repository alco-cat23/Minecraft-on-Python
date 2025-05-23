
from turtle import position, pu
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# загрузка ассетов
grass_texture = load_texture("Assets/Textures/Grass_Block.png")
bookshelf_texture = load_texture("Assets/Textures/Bookshelf.png")
coal_ore_texture = load_texture("Assets/Textures/Coal_Ore_Block.png")
stone_texture = load_texture("Assets/Textures/Stone_Block.png")
brick_texture = load_texture("Assets/Textures/Brick_Block.png")
dirt_texture = load_texture("Assets/Textures/Dirt_Block.png")
wood_texture = load_texture("Assets/Textures/Wood_Block.png")
sky_texture = load_texture("Assets/Textures/Skybox.png")
arm_texture = load_texture("Assets/Textures/Arm_Texture.png")
punch_sound = Audio("Assets/SFX/Punch_Sound.wav", loop=False, autoplay=False)
window.exit_button.visible = False
block_pick = 1


# Взаимодействие с инвентарём
def update():
    global block_pick

    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5
    if held_keys["6"]: block_pick = 6
    if held_keys["7"]: block_pick = 7
    if held_keys["8"]: block_pick = 8
    if held_keys["9"]: block_pick = 9


# Voxel (блоки)
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=dirt_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="Assets/Models/Block",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=0.5
        )

    # Взаимодействие блоков

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                punch_sound.play()
                if block_pick == 1: Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5: Voxel(position=self.position + mouse.normal, texture=wood_texture)
                if block_pick == 6: Voxel(position=self.position + mouse.normal, texture=coal_ore_texture)
                if block_pick == 7: Voxel(position=self.position + mouse.normal, texture=bookshelf_texture)

            if key == "left mouse down":
                punch_sound.play()
                destroy(self)
                
            if key == "alt+f4":
                var = app.close_window

            if key == "e" or key == "E":
                pass


# Небо
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="Sphere",
            texture=sky_texture,
            scale=1000,
            double_sided=True
        )


# Создание руки
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="Assets/Models/Arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


# Создание карты мира
for z in range(20):
    for y in range(2):
        for x in range(20):
            voxel = Voxel(position=(x, y, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
