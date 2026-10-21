import tkinter as tk
from tkinter import font as tkfont
import math
import random



QUESTIONS = [
    {
        "text": "Kündekari hangi malzemeyle yapılır?",
        "options": ["Cam", "Ahşap", "Mermer", "Kumaş"],
        "answer": 1,
    },
    {
        "text": "Hakiki kündekari tekniğinin en önemli özelliği nedir?",
        "options": [
            "Çivi ve tutkal kullanılmaması",
            "Plastik malzeme kullanılması",
            "Parçaların iple bağlanması",
            "Yüzeyin boyanması",
        ],
        "answer": 0,
    },
    {
        "text": "Kündekari parçalarının birbirine kilitlenmesini sağlayan sistem hangisidir?",
        "options": ["Geçme tekniği", "Kaynak tekniği", "Dikiş tekniği", "Yapıştırma tekniği"],
        "answer": 0,
    },
    {
        "text": "Kündekari ustalığıyla uğraşan ahşap zanaatkârına ne denir?",
        "options": ["Hattat", "Mücellit", "Neccar", "Nakkaş"],
        "answer": 2,
    },
    {
        "text": "Kündekaride tek parça ahşap yerine neden çok sayıda küçük parça kullanılır?",
        "options": [
            "Ahşabın nemden çatlamasını ve eğilmesini önlemek için",
            "Taşınması hafif olsun diye",
            "Ucuz olduğu için",
            "Daha hızlı üretim için",
        ],
        "answer": 0,
    },
    {
        "text": "Kündekari yüzeylerinde en çok hangi motifler kullanılır?",
        "options": [
            "İnsan resmi",
            "Geometrik ve yıldız motifleri",
            "Hayvan figürleri",
            "Manzara resimleri",
        ],
        "answer": 1,
    },
    {
        "text": "Kündekari en parlak dönemini hangi devletler zamanında yaşamıştır?",
        "options": ["Selçuklu ve Osmanlı", "Göktürk", "Roma", "Sümer"],
        "answer": 0,
    },
    {
        "text": "Kündekari yüzeyine sedef veya fildişi yerleştirilmesi sanatına ne ad verilir?",
        "options": ["Ebru", "Kakmacılık", "Çinicilik", "Dokumacılık"],
        "answer": 1,
    },
    {
        "text": "Kündekari yapımında en sık tercih edilen dayanıklı ağaç hangisidir?",
        "options": ["Ceviz / Abanoz", "Söğüt", "Kavak", "Çam çıtası"],
        "answer": 0,
    },
    {
        "text": "İyi korunmuş bir kündekari sanatı kaç yıl dayanabilir?",
        "options": ["10 yıl", "50 yıl", "Yüzyıllarca", "2 yıl"],
        "answer": 2,
    },
    {
        "text": "Parçaların düz bir panoya yapıştırılmasıyla yapılan pratik yönteme ne denir?",
        "options": [
            "Yalancı (Çakma) Kündekari",
            "Hızlı Kündekari",
            "Plastik Kündekari",
            "Modern Kündekari",
        ],
        "answer": 0,
    },
    {
        "text": "Kündekari sanatının temel amacı nedir?",
        "options": [
            "Ahşabı hızlı tüketmek",
            "Çivisiz ve uzun ömürlü ahşap yapılar üretmek",
            "Yüzeyleri renklendirmek",
            "Kağıda desen çizmek",
        ],
        "answer": 1,
    },
    {
        "text": "Kündekari tekniği camilerde en çok hangi bölümde görülür?",
        "options": ["Minber ve kapılarda", "Şadırvanda", "Minarede", "Halılarda"],
        "answer": 0,
    },
    {
        "text": "Güneş Sistemi motifli ünlü kündekari minber hangi camidedir?",
        "options": [
            "Bursa Ulu Camii",
            "Sultanahmet Camii",
            "Selimiye Camii",
            "Kocatepe Camii",
        ],
        "answer": 0,
    },
    {
        "text": "UNESCO Dünya Mirası Listesi'ndeki ahşap direkli ve kündekari işçilikli tarihi camimiz hangisidir?",
        "options": [
            "Beyşehir Eşrefoğlu Camii",
            "Ortaköy Camii",
            "Dolmabahçe Camii",
            "Şakirin Camii",
        ],
        "answer": 0,
    },
]


STAGES = [
    {
        "title": "Bölüm 1/5: Kündekari Atölyesi",
        "color": "#e8d5b5",
        "intro": "Dede Korkut: Kündekari mirasını korumak senin elinde!",
        "character": "Dede Korkut",
        "character_color": "#8b4b32",
        "character_position": (850, 560),
        "dialog": "Ben Dede Korkut. Oğuz anlatılarının bilge ozanıyım; ustalığın sırrı sabırdır.",
        "places": [(70, 120, 240, 220, "Kündekari Atölyesi")],
        "location_description": "Kündekari, küçük boyuttaki geometrik ahşap parçalarının çivi veya yapıştırıcı (tutkal) kullanılmadan, sadece birbirine geçmeli (zıvanalı/kinişli) şekilde kilitlenerek düz yüzeyler oluşturulmasıyla yapılan geleneksel bir Türk-İslam ahşap işçiliği sanatıdır.",
    },
    {
        "title": "Bölüm 2/5: Kakma Atölyesi",
        "color": "#d7e8d2",
        "intro": "Ahi Evran: Küçük parçaların uyumunu keşfet.",
        "character": "Ahi Evran",
        "character_color": "#3c7864",
        "character_position": (850, 560),
        "dialog": "Ben Ahi Evran. Zanaatında dürüstlük ve emeğe saygı önemlidir.",
        "places": [(70, 120, 250, 230, "KAKMA")],
        "location_description": "Kakma Sanatı, ahşap, taş veya metal yüzeylerde açılan oyuklara sedef, fildişi, kemik, gümüş tel ya da farklı renkte zıt malzeme parçalarının tam oturacak şekilde yerleştirilmesiyle yapılan bir yüzey süsleme (dekorasyon) sanatıdır.",
    },
    {
        "title": "Bölüm 3/5 Anadolu Selçuklu Mimarisinde Kündekari",
        "color": "#d6e3ed",
        "intro": "Mimar Sinan: Ustaların izinden ilerliyorsun.",
        "character": "Mimar Sinan",
        "character_color": "#526c8a",
        "character_position": (850, 560),
        "dialog": "Bir binanın güzelliği, parçalarının birbirine olan oranında ve o oranların yarattığı ahenktedir.",
        "places": [(70, 120, 250, 250, "UNESCO Dünya Mirası (2023)")],
        "location_description": "Beyşehir Eşrefoğlu Camii (Konya - 1299): Anadolu Selçuklu ve Beylikler döneminin ahşap mimarideki en görkemli yapısıdır. İçerisindeki 48 adet ahşap sütunu, ahşap konsolları ve kalem işi süslemelerinin yanı sıra minberi, kapı kanatları ve pencere kapakları tamamen kündekârî tekniğiyle yapılmıştır. Anadolu’nun ahşap tavanlı ve ahşap destekli camilerinin en büyüğüdür.",
    },
    {
        "title": "Bölüm 4/5 Bursa Ulu Cami Minberi",
        "color": "#ead9c5",
        "intro": "Yıldırım Bayezid: Son mühürler yaklaşıyor.",
        "character": "Yıldırım Bayezid",
        "character_color": "#76523d",
        "character_position": (850, 560),
        "dialog": "Bursa Ulu Cami, benim padişahlık dönemimde yapılmıştır. Minberin kündekârî ustası ise Antepli Mehmed oğlu Hacı Muhammed'dir. Kullanılan ahşap parça sayısının (yaklaşık 6.666 adet) İslam dininin kutsal kitabı Kur'an’daki ayet sayısına denk getirildiği ifade edilir. Minberin doğu cephesindeki geometrik kabartma desenlerin ise Güneş Sistemi'ni ve gezegenlerin dizilimini sembolize ettiği kabul edilir.",
        "places": [(70, 120, 250, 230, "MİNBER")],
        "location_description": "Minber, cuma ve bayram namazlarında hutbe okumak amacıyla camilerde mihrabın sağına yapılan; süslü kapısı, merdiveni ve özellikle kündekârî ahşap sanatının en nadide örneklerinin sergilendiği mimari yapıdır.",
    },
    {
        "title": "Bölüm 5/5: Mevlânâ Celâleddîn-i Rûmî (UNESCO Mevlana and Tolerance Year/2007)",
        "color": "#dce6e2",
        "intro": "Mevlânâ Celâleddîn-i Rûmî: Mirasın son sınavına hoş geldin!",
        "character": "Mevlânâ Celâleddîn-i Rûmî",
        "character_color": "#47776e",
        "character_position": (850, 560),
        "dialog": "Ben Mevlânâ Celâleddîn-i Rûmî, anlayış ve sevgi felsefesiyle tüm insanlığa kucak açan 13. yüzyıl tasavvuf alimi ve şairiyim. Konya’daki türbemde sanduka muhafazalarında, kapılarda ve rahlelerde kündekârî örneklerini görebilirsiniz.",
        "places": [(70, 120, 250, 250, "MİRAS SANDIĞI")],
        "location_description": "Kündekârî sanatı, neme ve sıcaklık değişimlerine karşı son derece dayanıklı bir ahşap geçme tekniği olduğu için saraylar, kasırlar, medreseler, şifahaneler, türbeler ve anıt mezarlarda da yoğun olarak kullanılmıştır.",
    },
]


class CippOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Kündekari Sanatı")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.fullscreen = True
        self.root.attributes("-fullscreen", self.fullscreen)

        self.canvas = tk.Canvas(root, width=1000, height=700, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.focus_set()
        self.font_metrics = {}

        self.root.bind("<KeyPress>", self.key_down)
        self.root.bind("<KeyRelease>", self.key_up)
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        self.canvas.bind("<Button-4>", self.mouse_wheel)
        self.canvas.bind("<Button-5>", self.mouse_wheel)

        self.game_state = "intro"
        self.keys = set()
        self.test_mode = False
        self.test_code = []
        self.stage = 1
        self.score = 0
        self.health = 5
        self.player_x = 500
        self.player_y = 550
        self.inventory = ["sword"]
        self.equipped_item = "sword"
        self.shield_block_frames = 0
        self.enemies = []
        self.projectiles = []
        self.enemy_projectiles = []
        self.seals = []
        self.active_seal = None
        self.hit_cooldown = 0
        self.attack_cooldown = 0
        self.sword_swing_frames = 0
        self.sword_swing_angle = -math.pi / 2
        self.message = ""
        self.frame_count = 0
        self.particles = []
        self.ambient_particles = []

        for _ in range(28):
            self.ambient_particles.append({
                "x": random.randint(0, 1000),
                "y": random.randint(50, 680),
                "speed": random.uniform(0.3, 1.0),
                "size": random.choice((2, 3, 4)),
            })

        self.draw_intro()
        self.root.after(33, self.game_loop)

    def start_game(self):
        self.stage = 1
        self.score = 0
        self.health = 5
        self.inventory = ["sword"]
        self.equipped_item = "sword"
        self.shield_block_frames = 0
        self.game_state = "playing"
        self.load_stage()

    def load_stage(self):
        self.player_x = 500
        self.player_y = 550
        self.hit_cooldown = 0
        self.attack_cooldown = 0
        self.sword_swing_frames = 0
        self.message = STAGES[self.stage - 1]["intro"]
        new_items = []
        if self.stage >= 2 and "shield" not in self.inventory:
            self.inventory.append("shield")
            new_items.append("Kalkan")
        if self.stage >= 3 and "ranged" not in self.inventory:
            self.inventory.append("ranged")
            new_items.append("Enerji küresi")
        if new_items:
            self.equipped_item = self.inventory[-1]
            self.message += " Yeni eşya: " + ", ".join(new_items) + ". I ile envanter."

        self.seals = []
        first_question = (self.stage - 1) * 3
        seal_positions = [(280, 350), (500, 350), (720, 350)]

        for number in range(3):
            x, y = seal_positions[number]
            self.seals.append({
                "x": x,
                "y": y,
                "question": first_question + number,
                "collected": False,
            })

        self.enemies = []
        self.projectiles = []
        self.enemy_projectiles = []
        enemy_count = self.stage + 5
        enemy_types = ("normal", "shielded", "armed")

        for number in range(enemy_count):
            enemy_x = 180 + (number % 5) * 160
            enemy_y = 170 + (number // 5) * 80
            enemy_type = enemy_types[number % len(enemy_types)]
            enemy_health = 3 + (self.stage - 1) // 2
            if enemy_type == "armed":
                enemy_health = max(2, enemy_health - 1)
            self.enemies.append({
                "x": enemy_x,
                "y": enemy_y,
                "type": enemy_type,
                "health": enemy_health,
                "max_health": enemy_health,
                "shield_active": enemy_type == "shielded",
                "shield_cooldown": 0,
                "shoot_cooldown": 45 + number * 13,
            })

        self.game_state = "dialog"

    def key_down(self, event):
        key = event.keysym.lower()
        self.test_code.append(key)
        self.test_code = self.test_code[-10:]

        if key == "f11":
            self.fullscreen = not self.fullscreen
            self.root.attributes("-fullscreen", self.fullscreen)
            return

        if self.game_state == "intro":
            if key in ("return", "space"):
                self.game_state = "menu"
            return

        if self.test_code == [
            "up", "up", "down", "down", "left",
            "right", "left", "right", "b", "a",
        ]:
            self.test_mode = not self.test_mode
            self.message = (
                "Test modu açıldı: mühür soruları atlanır."
                if self.test_mode
                else "Test modu kapatıldı."
            )
            self.test_code.clear()

        if self.game_state == "menu":
            if key in ("1", "return"):
                self.start_game()
            elif key == "2":
                self.game_state = "howto"
            elif key == "3":
                self.game_state = "about"
            elif key == "4":
                self.root.quit()
            return

        if self.game_state in ("howto", "about"):
            if key in ("escape", "return"):
                self.game_state = "menu"
            return

        if self.game_state == "dialog":
            if key in ("e", "space", "return", "escape"):
                self.game_state = "playing"
            return

        if self.game_state in ("victory", "game_over"):
            if key == "return":
                self.game_state = "menu"
            return

        if self.game_state == "paused":
            if key == "p":
                self.game_state = "playing"
            elif key == "r":
                self.start_game()
            elif key == "escape":
                self.game_state = "menu"
            return

        if self.game_state == "inventory":
            if key in ("i", "escape"):
                self.game_state = "playing"
            elif key in ("1", "2", "3"):
                self.select_inventory_item(int(key) - 1)
            return

        if self.game_state == "quiz":
            if key in ("1", "2", "3", "4"):
                self.answer_question(int(key) - 1)
            return

        if key in ("escape", "p"):
            self.game_state = "paused"
        elif key == "i":
            self.game_state = "inventory"
        elif key == "space":
            if key not in self.keys:
                self.keys.add(key)
                self.attack()
        elif key == "e":
            self.interact()
        else:
            self.keys.add(key)

    def key_up(self, event):
        key = event.keysym.lower()
        self.keys.discard(key)

    def select_inventory_item(self, index):
        if index >= len(self.inventory):
            return

        self.equipped_item = self.inventory[index]
        self.game_state = "playing"
        item_names = {
            "sword": "Kılıç",
            "shield": "Kalkan",
            "ranged": "Enerji küresi",
        }
        self.message = item_names[self.equipped_item] + " seçildi."

    def cycle_inventory(self, direction):
        if self.game_state not in ("playing", "inventory") or len(self.inventory) < 2:
            return

        current_index = self.inventory.index(self.equipped_item)
        next_index = (current_index + direction) % len(self.inventory)
        self.select_inventory_item(next_index)

    def mouse_wheel(self, event):
        if getattr(event, "num", None) == 4:
            direction = -1
        elif getattr(event, "num", None) == 5:
            direction = 1
        else:
            direction = -1 if event.delta > 0 else 1
        self.cycle_inventory(direction)

    def move_player(self):
        change_x = 0
        change_y = 0

        if "a" in self.keys or "left" in self.keys:
            change_x -= 1
        if "d" in self.keys or "right" in self.keys:
            change_x += 1
        if "w" in self.keys or "up" in self.keys:
            change_y -= 1
        if "s" in self.keys or "down" in self.keys:
            change_y += 1

        distance = math.hypot(change_x, change_y)
        if distance > 0:
            self.player_x += change_x / distance * 4
            self.player_y += change_y / distance * 4

        self.player_x = max(25, min(975, self.player_x))
        self.player_y = max(70, min(570, self.player_y))

    def move_enemies(self):
        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        for enemy in self.enemies:
            if enemy["type"] == "shielded" and not enemy["shield_active"]:
                enemy["shield_cooldown"] -= 1
                if enemy["shield_cooldown"] <= 0:
                    enemy["shield_active"] = True

            difference_x = self.player_x - enemy["x"]
            difference_y = self.player_y - enemy["y"]
            distance = math.hypot(difference_x, difference_y)
            enemy_type = enemy["type"]

            if enemy_type == "normal" and distance > 28:
                speed = 2.0 + self.stage * 0.3
                enemy["x"] += difference_x / distance * speed
                enemy["y"] += difference_y / distance * speed
            elif enemy_type == "shielded" and distance > 28:
                speed = 1.4 + self.stage * 0.18
                enemy["x"] += difference_x / distance * speed
                enemy["y"] += difference_y / distance * speed
            elif enemy_type == "armed":
                speed = 1.5 + self.stage * 0.16
                if distance > 250:
                    enemy["x"] += difference_x / distance * speed
                    enemy["y"] += difference_y / distance * speed
                elif distance < 150 and distance > 0:
                    enemy["x"] -= difference_x / distance * speed
                    enemy["y"] -= difference_y / distance * speed

                enemy["shoot_cooldown"] -= 1
                if enemy["shoot_cooldown"] <= 0 and distance > 0:
                    projectile_speed = 5
                    self.enemy_projectiles.append({
                        "x": enemy["x"],
                        "y": enemy["y"],
                        "vx": difference_x / distance * projectile_speed,
                        "vy": difference_y / distance * projectile_speed,
                        "life": 100,
                        "owner": enemy,
                    })
                    enemy["shoot_cooldown"] = max(55, 105 - self.stage * 8)
            elif self.hit_cooldown == 0:
                self.damage_player("Düşman sana dokundu!")

            if enemy_type != "armed" and distance <= 28 and self.hit_cooldown == 0:
                self.damage_player("Düşman sana dokundu!")

    def damage_player(self, message):
        if self.shield_block_frames > 0:
            self.shield_block_frames = 0
            self.hit_cooldown = 15
            self.message = "Kalkan darbeyi engelledi!"
            self.spawn_particles(self.player_x, self.player_y, "#73c7dc")
            return

        self.health -= 1
        self.hit_cooldown = 30
        self.message = message
        self.spawn_particles(self.player_x, self.player_y, "#e45b55")
        if self.health <= 0:
            self.game_state = "game_over"

    def update_enemy_projectiles(self):
        for projectile in self.enemy_projectiles[:]:
            projectile["x"] += projectile["vx"]
            projectile["y"] += projectile["vy"]
            projectile["life"] -= 1

            hit_enemy = next((
                enemy for enemy in self.enemies
                if enemy is not projectile["owner"] and math.hypot(
                    projectile["x"] - enemy["x"],
                    projectile["y"] - enemy["y"],
                ) < 20
            ), None)

            if hit_enemy is not None:
                self.enemy_projectiles.remove(projectile)
                self.hit_enemy(hit_enemy, award_score=False)
            elif math.hypot(
                projectile["x"] - self.player_x,
                projectile["y"] - self.player_y,
            ) < 20:
                self.enemy_projectiles.remove(projectile)
                if self.hit_cooldown == 0:
                    self.damage_player("Uzaktan saldıran düşmanın küresi isabet etti!")
            elif projectile["life"] <= 0:
                self.enemy_projectiles.remove(projectile)

    def spawn_particles(self, x, y, color):
        for _ in range(8):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(1, 3)
            self.particles.append({
                "x": x,
                "y": y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "life": 18,
                "color": color,
            })

    def attack(self):
        if self.attack_cooldown > 0:
            return

        if self.equipped_item == "shield":
            self.shield_block_frames = 36
            self.attack_cooldown = 45
            self.message = "Kalkanını kaldırdın!"
            return

        if self.equipped_item == "sword":
            self.sword_swing_frames = 8

        closest_enemy = None
        attack_range = 100 if self.equipped_item == "sword" else 460
        closest_distance = attack_range

        for enemy in self.enemies:
            distance = math.hypot(
                self.player_x - enemy["x"],
                self.player_y - enemy["y"],
            )
            if distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance

        if closest_enemy is not None:
            if self.equipped_item == "sword":
                self.attack_cooldown = 18
                self.sword_swing_angle = math.atan2(
                    closest_enemy["y"] - self.player_y,
                    closest_enemy["x"] - self.player_x,
                )
                self.hit_enemy(closest_enemy)
                return

            difference_x = closest_enemy["x"] - self.player_x
            difference_y = closest_enemy["y"] - self.player_y
            distance = math.hypot(difference_x, difference_y)
            projectile_speed = 9
            self.projectiles.append({
                "x": self.player_x,
                "y": self.player_y,
                "vx": difference_x / distance * projectile_speed,
                "vy": difference_y / distance * projectile_speed,
                "life": 60,
            })
            self.attack_cooldown = 24
            self.message = "Enerji küresi gönderildi!"
        elif self.equipped_item == "sword":
            self.attack_cooldown = 18
            self.sword_swing_angle = -math.pi / 2
            self.message = "Kılıç savruldu. Düşmana biraz yaklaş."
        else:
            self.message = "Menzilde düşman yok."

    def hit_enemy(self, enemy, award_score=True):
        if enemy["type"] == "shielded" and enemy["shield_active"]:
            enemy["shield_active"] = False
            enemy["shield_cooldown"] = 120
            particle_color = "#73c7dc"
            self.message = "Kalkan kırıldı! Açıkken saldır."
        else:
            enemy["health"] -= 1
            if enemy["health"] <= 0:
                self.enemies.remove(enemy)
                if award_score:
                    self.score += 20
                particle_color = "#ffd166"
                self.message = "Bir düşmanı yendin!"
            else:
                particle_color = "#e98555"
                self.message = "Düşman yaralandı!"
        self.spawn_particles(enemy["x"], enemy["y"], particle_color)

    def update_projectiles(self):
        for projectile in self.projectiles[:]:
            projectile["x"] += projectile["vx"]
            projectile["y"] += projectile["vy"]
            projectile["life"] -= 1

            hit_enemy = next((
                enemy for enemy in self.enemies
                if math.hypot(
                    projectile["x"] - enemy["x"],
                    projectile["y"] - enemy["y"],
                ) < 20
            ), None)

            if hit_enemy is not None:
                self.projectiles.remove(projectile)
                self.hit_enemy(hit_enemy)
            elif projectile["life"] <= 0:
                self.projectiles.remove(projectile)

    def interact(self):
        stage_info = STAGES[self.stage - 1]
        character_x, character_y = stage_info["character_position"]
        distance_to_character = math.hypot(
            self.player_x - character_x,
            self.player_y - character_y,
        )

        if distance_to_character < 60:
            self.game_state = "dialog"
            return

        for seal in self.seals:
            if seal["collected"]:
                continue

            distance = math.hypot(
                self.player_x - seal["x"],
                self.player_y - seal["y"],
            )
            if distance < 55:
                if self.test_mode:
                    seal["collected"] = True
                    self.score += 100
                    self.message = "Test modu: mühür sorusu atlandı."
                    self.spawn_particles(seal["x"], seal["y"], "#53c9a5")
                else:
                    self.active_seal = seal
                    self.game_state = "quiz"
                return

        if self.stage_is_complete():
            distance_to_gate = math.hypot(self.player_x - 500, self.player_y - 90)
            if distance_to_gate < 60:
                if self.stage == len(STAGES):
                    self.game_state = "victory"
                else:
                    self.stage += 1
                    self.load_stage()

    def answer_question(self, selected_option):
        question = QUESTIONS[self.active_seal["question"]]

        if selected_option == question["answer"]:
            self.active_seal["collected"] = True
            self.score += 100
            self.message = "Doğru cevap! Mühür açıldı."
            self.spawn_particles(
                self.active_seal["x"], self.active_seal["y"], "#53c9a5"
            )
        else:
            self.health -= 1
            self.message = "Yanlış cevap. Bir can kaybettin."
            self.spawn_particles(
                self.active_seal["x"], self.active_seal["y"], "#e45b55"
            )

        self.active_seal = None
        self.game_state = "playing"

        if self.health <= 0:
            self.game_state = "game_over"

    def stage_is_complete(self):
        all_seals_found = all(seal["collected"] for seal in self.seals)
        all_enemies_defeated = len(self.enemies) == 0
        return all_seals_found and all_enemies_defeated

    def update_game(self):
        self.frame_count += 1

        for particle in self.ambient_particles:
            particle["y"] -= particle["speed"]
            if particle["y"] < 45:
                particle["y"] = 680
                particle["x"] = random.randint(0, 1000)

        for particle in self.particles[:]:
            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]
            particle["life"] -= 1
            if particle["life"] <= 0:
                self.particles.remove(particle)

        if self.game_state == "playing":
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1
            if self.shield_block_frames > 0:
                self.shield_block_frames -= 1
            if self.sword_swing_frames > 0:
                self.sword_swing_frames -= 1
            self.move_player()
            self.move_enemies()
            self.update_projectiles()
            self.update_enemy_projectiles()

    def draw_menu(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#173746")
        self.canvas.create_polygon(
            0, 440, 180, 300, 360, 440, 560, 270, 790, 430,
            1000, 290, 1000, 700, 0, 700,
            fill="#245563", outline="",
        )
        self.canvas.create_polygon(
            0, 540, 240, 430, 470, 550, 730, 410, 1000, 530,
            1000, 700, 0, 700,
            fill="#172f3b", outline="",
        )
        for particle in self.ambient_particles:
            self.canvas.create_oval(
                particle["x"], particle["y"],
                particle["x"] + particle["size"],
                particle["y"] + particle["size"],
                fill="#f6d98b", outline="",
            )
        self.canvas.create_text(
            500, 170, text="Kündekari Sanatı", fill="#f6d98b",
            font=("Georgia", 40, "bold"),
        )
        self.canvas.create_text(
            500, 230, text="Kündekari Mirası", fill="#f4eee2",
            font=("Georgia", 22),
        )
        self.canvas.create_text(
            500, 280, text="Miras Sandığı", fill="#f6d98b",
            font=("Georgia", 17, "bold"),
        )
        self.canvas.create_text(
            500, 345,
            text=(
                "Bu sandık, dededen toruna, ustadan çırağa devredilen bir hazinedir. "
                "İçinde altın, gümüş değil; sabır, emek ve nesilden nesile aktarılması "
                "gereken çevre dostu bir sanatın sırları saklıdır."
            ),
            fill="#f4eee2", width=720, justify="center",
            font=("Arial", 12),
        )
        
        self.canvas.create_text(
            500,
            440,
            text="1: Oyuna başla     2: Nasıl oynanır?     3: Hakkında     4: Çıkış",
            fill="#f4eee2", font=("Arial", 14),
        )

        self.canvas.create_text(
            100,
            650,
            text="WASD/Yön: hareket   SPACE: eşya kullan   I: envanter   P: duraklat",
            fill="#003f24", font=("Arial", 10),
        )


    def draw_intro(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#e8d5b5")
        self.canvas.create_rectangle(
            65, 95, 765, 610,
            fill="#fffdf7", outline="#493722", width=3,
        )
        self.canvas.create_text(
            415, 145, text="Gölge Usta", fill="#111111",
            font=("Georgia", 30, "bold"),
        )
        self.canvas.create_text(
            415, 235,
            text=(
                "Selam yolcu. Ben Gölge Usta. Kündekari mirasını korumak "
                "için mühürleri topla, soruları cevapla ve beş bölümü tamamla. "
                "Karşına çıkan düşmanları uygun eşyanla yen; kalkanlıların "
                "kalkanı açıldığında harekete geç."
            ),
            width=590, justify="left", font=("Arial", 16),
        )
        self.canvas.create_text(
            415, 390,
            text=(
                "WASD / yön tuşları: hareket\n"
                "SPACE: seçili eşyayı kullan    E: etkileşim\n"
                "Fare tekerleği: eşya değiştir    I: envanter\n"
                "P: duraklat\n"
                "F11: tam ekran\n"
                "Duraklatınca R: yeniden başlat"
            ),
            width=590, justify="left", font=("Arial", 14, "bold"),
        )
        self.canvas.create_polygon(
            860, 250, 812, 300, 785, 490, 935, 490, 908, 300,
            fill="#000000", outline="#000000",
        )
        self.canvas.create_oval(
            818, 205, 902, 310,
            fill="#000000", outline="#000000",
        )
        self.canvas.create_oval(
            835, 258, 850, 265, fill="#ffffff", outline="#ffffff",
        )
        self.canvas.create_oval(
            870, 258, 885, 265, fill="#ffffff", outline="#ffffff",
        )
        self.canvas.create_text(
            415, 560, text="Devam etmek için ENTER veya SPACE",
            fill="#493722", font=("Arial", 12, "bold"),
        )

    def draw_information_page(self, title, text):
        self.canvas.delete("all")
        self.canvas.configure(bg="#e8e3d7")
        self.canvas.create_text(500, 150, text=title, font=("Georgia", 26, "bold"))
        self.canvas.create_text(
            500, 320, text=text, width=700, justify="center", font=("Arial", 15)
        )
        self.canvas.create_text(
            500, 600, text="Menüye dönmek için ENTER", font=("Arial", 12)
        )

    def draw_character(self):
        stage_info = STAGES[self.stage - 1]
        x, y = stage_info["character_position"]
        color = stage_info["character_color"]

        self.canvas.create_oval(
            x - 30, y - 42, x + 30, y + 24,
            outline="#fff2c2", width=2,
        )
        self.canvas.create_polygon(
            x - 20, y + 28, x - 15, y - 5, x + 15, y - 5, x + 20, y + 28,
            fill=color, outline="#493722", width=2,
        )
        self.canvas.create_oval(
            x - 11, y - 30, x + 11, y - 8,
            fill="#d8b18a", outline="#493722",
        )
        self.canvas.create_arc(
            x - 14, y - 36, x + 14, y - 15,
            start=0, extent=180, fill="#f2c14e", outline="#493722",
        )
        self.canvas.create_text(
            x, y + 48, text=stage_info["character"],
            fill="#33271e", font=("Arial", 10, "bold"),
        )

    def draw_dialog(self):
        stage_info = STAGES[self.stage - 1]
        self.canvas.create_rectangle(
            170, 500, 830, 625,
            fill="#fffdf7", outline="#493722", width=3,
        )
        self.canvas.create_text(
            500, 530, text=stage_info["character"],
            font=("Arial", 15, "bold"),
        )
        self.canvas.create_text(
            500, 570, text=stage_info["dialog"],
            width=590, justify="center", font=("Arial", 12),
        )
        self.canvas.create_text(
            500, 610, text="Devam etmek için E tuşuna bas",
            font=("Arial", 10),
        )

    def draw_game(self):
        stage_info = STAGES[self.stage - 1]
        self.canvas.delete("all")
        self.canvas.configure(bg=stage_info["color"])

        for x in range(30, 1000, 50):
            self.canvas.create_line(x, 55, x, 690, fill="#ffffff", stipple="gray12")
        for y in range(55, 700, 50):
            self.canvas.create_line(0, y, 1000, y, fill="#ffffff", stipple="gray12")

        for particle in self.ambient_particles:
            self.canvas.create_oval(
                particle["x"], particle["y"],
                particle["x"] + particle["size"],
                particle["y"] + particle["size"],
                fill="#fff2c2", outline="",
            )

        self.canvas.create_text(
            500,
            25,
            text=stage_info["title"],
            font=("Arial", 16, "bold"),
        )
        self.canvas.create_text(
            130, 25, text=f"Can: {self.health}", font=("Arial", 13, "bold")
        )
        self.canvas.create_text(
            870, 25, text=f"Puan: {self.score}", font=("Arial", 13, "bold")
        )
        self.canvas.create_rectangle(
            12, 45, 800, 118, fill="#fffdf7", outline="#493722", width=2
        )
        self.canvas.create_text(
            24, 51, text=stage_info["places"][0][4],
            anchor="nw", font=("Arial", 11, "bold"),
        )
        self.canvas.create_text(
            24, 73, text=stage_info["location_description"],
            anchor="nw", width=760, justify="left", font=("Arial", 7),
        )

        for x1, y1, x2, y2, name in stage_info["places"]:
            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill="#9b7653", outline="#493722", width=2
            )
            self.canvas.create_text(
                (x1 + x2) / 2, (y1 + y2) / 2, text=name, width=x2 - x1 - 10
            )

            self.draw_character()

        for seal in self.seals:
            pulse = math.sin(self.frame_count / 5) * 3
            radius = 20 + pulse
            color = "#55b99a" if seal["collected"] else "#f2c14e"
            self.canvas.create_oval(
                seal["x"] - radius - 5,
                seal["y"] - radius - 5,
                seal["x"] + radius + 5,
                seal["y"] + radius + 5,
                outline="#fff2c2",
                width=2,
            )
            self.canvas.create_oval(
                seal["x"] - radius,
                seal["y"] - radius,
                seal["x"] + radius,
                seal["y"] + radius,
                fill=color,
                outline="#493722",
                width=2,
            )
            self.canvas.create_text(
                seal["x"], seal["y"], text="✓" if seal["collected"] else "✦",
                fill="#fffdf7", font=("Arial", 13, "bold"),
            )

        for enemy in self.enemies:
            enemy_type = enemy["type"]
            enemy_colors = {
                "normal": "#b5443c",
                "shielded": "#397e9b",
                "armed": "#bd762f",
            }
            if enemy_type == "armed" and 0 < enemy["shoot_cooldown"] <= 15:
                self.canvas.create_line(
                    enemy["x"], enemy["y"], self.player_x, self.player_y,
                    fill="#e45b55", dash=(4, 3), width=2,
                )
            self.canvas.create_oval(
                enemy["x"] - 15,
                enemy["y"] - 15,
                enemy["x"] + 15,
                enemy["y"] + 15,
                fill=enemy_colors[enemy_type],
                outline="#61221e",
                width=2,
            )
            if enemy_type == "shielded":
                self.canvas.create_oval(
                    enemy["x"] - 19,
                    enemy["y"] - 19,
                    enemy["x"] + 19,
                    enemy["y"] + 19,
                    outline=("#73c7dc" if enemy["shield_active"] else "#69777a"),
                    width=3,
                )
            type_labels = {
                "normal": "Normal",
                "shielded": "Kalkanlı",
                "armed": "Uzaktan saldıran",
            }
            self.canvas.create_text(
                enemy["x"], enemy["y"] - 31,
                text=type_labels[enemy_type],
                fill="#26353b",
                font=("Arial", 8, "bold"),
            )
            health_width = 30 * enemy["health"] / enemy["max_health"]
            self.canvas.create_rectangle(
                enemy["x"] - 15,
                enemy["y"] - 23,
                enemy["x"] + 15,
                enemy["y"] - 19,
                fill="#fffdf7",
                outline="#61221e",
            )
            self.canvas.create_rectangle(
                enemy["x"] - 15,
                enemy["y"] - 23,
                enemy["x"] - 15 + health_width,
                enemy["y"] - 19,
                fill="#c9483f",
                outline="",
            )

        for projectile in self.projectiles:
            self.canvas.create_oval(
                projectile["x"] - 5,
                projectile["y"] - 5,
                projectile["x"] + 5,
                projectile["y"] + 5,
                fill="#ffd166",
                outline="#8a5a13",
                width=1,
            )

        for projectile in self.enemy_projectiles:
            self.canvas.create_oval(
                projectile["x"] - 5,
                projectile["y"] - 5,
                projectile["x"] + 5,
                projectile["y"] + 5,
                fill="#55a99a",
                outline="#286b61",
                width=1,
            )

        player_color = "#287a68"
        self.canvas.create_oval(
            self.player_x - 23,
            self.player_y - 23,
            self.player_x + 23,
            self.player_y + 23,
            outline="#fff2c2",
            width=2,
        )
        self.canvas.create_oval(
            self.player_x - 16,
            self.player_y - 16,
            self.player_x + 16,
            self.player_y + 16,
            fill=player_color,
            outline="#123f38",
            width=2,
        )
        if self.sword_swing_frames > 0:
            progress = (8 - self.sword_swing_frames) / 7
            swing_angle = self.sword_swing_angle + math.radians(
                (progress - 0.5) * 100
            )
            sword_start_x = self.player_x + math.cos(swing_angle) * 12
            sword_start_y = self.player_y + math.sin(swing_angle) * 12
            sword_end_x = self.player_x + math.cos(swing_angle) * 82
            sword_end_y = self.player_y + math.sin(swing_angle) * 82
            self.canvas.create_line(
                sword_start_x, sword_start_y, sword_end_x, sword_end_y,
                fill="#493722", width=10, capstyle=tk.ROUND,
            )
            self.canvas.create_line(
                sword_start_x, sword_start_y, sword_end_x, sword_end_y,
                fill="#f5e3a1", width=5, capstyle=tk.ROUND,
            )
        if self.shield_block_frames > 0:
            self.canvas.create_oval(
                self.player_x - 27,
                self.player_y - 27,
                self.player_x + 27,
                self.player_y + 27,
                outline="#73c7dc",
                width=3,
            )

        for particle in self.particles:
            size = max(1, particle["life"] // 5)
            self.canvas.create_oval(
                particle["x"] - size,
                particle["y"] - size,
                particle["x"] + size,
                particle["y"] + size,
                fill=particle["color"],
                outline="",
            )

        if self.stage_is_complete():
            pulse = math.sin(self.frame_count / 4) * 7
            self.canvas.create_oval(
                465 - pulse, 65 - pulse, 535 + pulse, 110 + pulse,
                outline="#b7f7c4", width=3,
            )
            self.canvas.create_rectangle(
                465, 65, 535, 110, fill="#438c54", outline="#174b2a", width=2
            )
            self.canvas.create_text(500, 125, text="Kapı: E", font=("Arial", 11))

        self.canvas.create_text(
            500,
            690,
            text="SPACE: eşya kullan   Fare tekerleği: değiştir   I: envanter   P: duraklat   F11: tam ekran",
            font=("Arial", 11),
        )
        self.canvas.create_text(
            500, 145, text=self.message, width=640, font=("Arial", 11)
        )
        self.draw_hotbar()

        if self.game_state == "quiz":
            self.draw_question()
        elif self.game_state == "paused":
            self.draw_overlay(
                "Oyun duraklatıldı",
                "P: devam et    R: yeniden başla\nESC: ana menü",
            )
        elif self.game_state == "inventory":
            self.draw_inventory()
        elif self.game_state == "dialog":
            self.draw_dialog()

    def draw_hotbar(self):
        item_names = {
            "sword": "Kılıç",
            "shield": "Kalkan",
            "ranged": "Küre",
        }
        self.canvas.create_rectangle(
            388, 596, 612, 669,
            fill="#26383b", outline="#e4d6a8", width=2,
        )
        self.canvas.create_text(
            500, 587, text="EŞYA DEĞİŞTİR: FARE TEKERLEĞİ",
            fill="#26383b", font=("Arial", 9, "bold"),
        )
        for index, item in enumerate(("sword", "shield", "ranged")):
            x1 = 396 + index * 69
            unlocked = item in self.inventory
            selected = item == self.equipped_item
            fill = "#f2c14e" if selected else "#fffdf7" if unlocked else "#697274"
            text_fill = "#26383b" if unlocked else "#d2d5d2"
            self.canvas.create_rectangle(
                x1, 604, x1 + 64, 661,
                fill=fill,
                outline="#fff2c2" if selected else "#829093",
                width=3 if selected else 1,
            )
            self.canvas.create_text(
                x1 + 8, 612, text=str(index + 1), anchor="nw",
                fill=text_fill, font=("Arial", 8, "bold"),
            )
            self.canvas.create_text(
                x1 + 32, 634,
                text=item_names[item] if unlocked else "Kilitli",
                fill=text_fill, font=("Arial", 10, "bold"),
            )

    def draw_inventory(self):
        item_names = {
            "sword": "Kılıç: yakın saldırı",
            "shield": "Kalkan: zamanlamalı savunma",
            "ranged": "Enerji küresi: uzak saldırı",
        }
        self.canvas.create_rectangle(
            250, 190, 750, 510,
            fill="#fffdf7", outline="#493722", width=3,
        )
        self.canvas.create_text(
            500, 230, text="Envanter", font=("Georgia", 22, "bold")
        )
        for index, item in enumerate(self.inventory):
            y = 295 + index * 58
            selected = item == self.equipped_item
            if selected:
                self.canvas.create_rectangle(
                    330, y - 21, 670, y + 21,
                    fill="#dcebe3", outline="#287a68", width=2,
                )
            self.canvas.create_text(
                500, y,
                text=f"{index + 1}. {item_names[item]}" + ("  [Seçili]" if selected else ""),
                font=("Arial", 14, "bold" if selected else "normal"),
            )
        self.canvas.create_text(
            500, 470, text="Sayı tuşuyla seç  |  I veya ESC ile kapat",
            font=("Arial", 11),
        )

    def draw_question(self):
        question = QUESTIONS[self.active_seal["question"]]
        self.canvas.create_rectangle(
            140, 180, 860, 535, fill="#fffdf7", outline="#493722", width=3
        )
        self.canvas.create_text(
            500, 220, text=question["text"], width=650, font=("Arial", 16, "bold")
        )

        for number, option in enumerate(question["options"], start=1):
            self.canvas.create_text(
                500,
                290 + (number - 1) * 48,
                text=f"{number}. {option}",
                width=650,
                font=("Arial", 13),
            )

        self.canvas.create_text(
            500, 500, text="Cevap için 1, 2, 3 veya 4 tuşuna bas", font=("Arial", 12)
        )

    def draw_overlay(self, title, text):
        self.canvas.create_rectangle(
            250, 260, 750, 420, fill="#fffdf7", outline="#493722", width=3
        )
        self.canvas.create_text(500, 315, text=title, font=("Arial", 22, "bold"))
        self.canvas.create_text(500, 370, text=text, font=("Arial", 13))

    def scale_canvas(self):
        canvas_width = max(1, self.canvas.winfo_width())
        canvas_height = max(1, self.canvas.winfo_height())
        scale = min(canvas_width / 1000, canvas_height / 700)
        offset_x = (canvas_width - 1000 * scale) / 2
        offset_y = (canvas_height - 700 * scale) / 2

        self.canvas.scale("all", 0, 0, scale, scale)
        self.canvas.move("all", offset_x, offset_y)

        for item in self.canvas.find_all():
            if self.canvas.type(item) != "text":
                continue
            font_description = self.canvas.itemcget(item, "font")
            if not font_description:
                continue
            if font_description not in self.font_metrics:
                font = tkfont.Font(root=self.root, font=font_description)
                actual_font = font.actual()
                self.font_metrics[font_description] = (
                    actual_font["family"],
                    abs(actual_font["size"]),
                    actual_font["weight"],
                    actual_font["slant"],
                )
            family, size, weight, slant = self.font_metrics[font_description]
            scaled_size = max(7, round(size * scale))
            self.canvas.itemconfigure(
                item, font=(family, scaled_size, weight, slant)
            )

    def game_loop(self):
        self.update_game()

        if self.game_state == "intro":
            self.draw_intro()
        elif self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "howto":
            self.draw_information_page(
                "Nasıl oynanır?",
                "WASD ile hareket et. I ile envanteri aç, sayı tuşlarıyla eşya seç. "
                "Fare tekerleğiyle açılmış eşyalar arasında geçiş yap. "
                "SPACE seçili eşyayı kullanır: kılıç yakın saldırı, kalkan savunma, "
                "enerji küresi uzak saldırı yapar. "
                "Normaller hızlıdır, kalkanlılar dayanıklıdır, uzaktan saldıranlar küre gönderir. "
                "P ile duraklat; duraklatma ekranında R ile yeniden başlat. "
                "F11 ile tam ekranı aç veya kapat. "
                "Mühürlerin yanına gelip E tuşuna bas ve soruları cevapla. "
                "Bölüm kapısını açmak için bütün mühürleri bul ve düşmanları yen. ",
            )
        elif self.game_state == "about":
            self.draw_information_page(
                "Kündekari hakkında",
                "Kündekari, küçük ahşap parçaların çivi ve tutkal kullanılmadan "
                "birbirine geçirilmesiyle yapılan geleneksel bir süsleme sanatıdır. "
                "Bu oyundaki sorular kündekari kültürel mirası hakkındadır.",
            )
        elif self.game_state in ("playing", "quiz", "paused", "dialog", "inventory"):
            self.draw_game()
        elif self.game_state == "game_over":
            self.draw_information_page(
                "Oyun bitti",
                f"Puanın: {self.score}. Menüye dönmek için ENTER tuşuna bas.",
            )
        elif self.game_state == "victory":
            self.draw_information_page(
                "Tebrikler!",
                f"Beş bölümü tamamladın. Toplam puanın: {self.score}. "
                "Menüye dönmek için ENTER tuşuna bas.",
            )

        self.scale_canvas()
        self.root.after(33, self.game_loop)


def main():
    root = tk.Tk()
    CippOyunu(root)
    root.mainloop()


if __name__ == "__main__":
    main()