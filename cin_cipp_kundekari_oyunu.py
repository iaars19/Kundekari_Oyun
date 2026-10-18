import tkinter as tk
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
            "Kolay kırıldığı için",
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
        "text": "İyi korunmuş bir kündekari eser ne kadar dayanabilir?",
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
        "title": "Bölüm 5/5: Mevlânâ Celâleddîn-i Rûmî",
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
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=1000, height=700, highlightthickness=0)
        self.canvas.pack()
        self.canvas.focus_set()

        self.root.bind("<KeyPress>", self.key_down)
        self.root.bind("<KeyRelease>", self.key_up)

        self.game_state = "menu"
        self.keys = set()
        self.test_mode = False
        self.test_code = []
        self.stage = 1
        self.score = 0
        self.health = 5
        self.player_x = 500
        self.player_y = 610
        self.enemies = []
        self.seals = []
        self.active_seal = None
        self.hit_cooldown = 0
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

        self.draw_menu()
        self.root.after(33, self.game_loop)

    def start_game(self):
        self.stage = 1
        self.score = 0
        self.health = 5
        self.game_state = "playing"
        self.load_stage()

    def load_stage(self):
        self.player_x = 500
        self.player_y = 610
        self.hit_cooldown = 0
        self.message = STAGES[self.stage - 1]["intro"]

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
        enemy_count = self.stage + 2

        for number in range(enemy_count):
            enemy_x = 180 + (number % 5) * 160
            enemy_y = 170 + (number // 5) * 90
            self.enemies.append({"x": enemy_x, "y": enemy_y})

    def key_down(self, event):
        key = event.keysym.lower()
        self.test_code.append(key)
        self.test_code = self.test_code[-10:]

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
            if key in ("escape", "p"):
                self.game_state = "playing"
            return

        if self.game_state == "quiz":
            if key in ("1", "2", "3", "4"):
                self.answer_question(int(key) - 1)
            return

        if key in ("escape", "p"):
            self.game_state = "paused"
        elif key == "space":
            self.attack()
        elif key == "e":
            self.interact()
        else:
            self.keys.add(key)

    def key_up(self, event):
        key = event.keysym.lower()
        self.keys.discard(key)

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
        self.player_y = max(70, min(660, self.player_y))

    def move_enemies(self):
        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        for enemy in self.enemies:
            difference_x = self.player_x - enemy["x"]
            difference_y = self.player_y - enemy["y"]
            distance = math.hypot(difference_x, difference_y)

            if distance > 28:
                speed = 1.2 + self.stage * 0.18
                enemy["x"] += difference_x / distance * speed
                enemy["y"] += difference_y / distance * speed
            elif self.hit_cooldown == 0:
                self.health -= 1
                self.hit_cooldown = 30
                self.message = "Düşman sana dokundu!"
                self.spawn_particles(self.player_x, self.player_y, "#e45b55")

                if self.health <= 0:
                    self.game_state = "game_over"

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
        closest_enemy = None
        closest_distance = 60

        for enemy in self.enemies:
            distance = math.hypot(
                self.player_x - enemy["x"],
                self.player_y - enemy["y"],
            )
            if distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance

        if closest_enemy is not None:
            self.enemies.remove(closest_enemy)
            self.score += 20
            self.message = "Bir düşmanı yendin!"
            self.spawn_particles(
                closest_enemy["x"], closest_enemy["y"], "#ffd166"
            )
        else:
            self.message = "Saldırmak için bir düşmana yaklaş."

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
            self.move_player()
            self.move_enemies()

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
            self.canvas.create_oval(
                enemy["x"] - 15,
                enemy["y"] - 15,
                enemy["x"] + 15,
                enemy["y"] + 15,
                fill="#b5443c",
                outline="#61221e",
                width=2,
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
            675,
            text="WASD: hareket   SPACE: saldırı   E: mühür/kapı   P: duraklat",
            font=("Arial", 11),
        )
        self.canvas.create_text(
            500, 645, text=self.message, width=920, font=("Arial", 11)
        )

        if self.game_state == "quiz":
            self.draw_question()
        elif self.game_state == "paused":
            self.draw_overlay("Oyun duraklatıldı", "Devam etmek için P veya ESC")
        elif self.game_state == "dialog":
            self.draw_dialog()

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

    def game_loop(self):
        self.update_game()

        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "howto":
            self.draw_information_page(
                "Nasıl oynanır?",
                "WASD ile hareket et. SPACE ile düşmanları yen. "
                "Mühürlerin yanına gelip E tuşuna bas ve soruları cevapla. "
                "Bölüm kapısını açmak için bütün mühürleri bul ve düşmanları yen. "
                "Test modu için sırayla: Yukarı, Yukarı, Aşağı, Aşağı, "
                "Sol, Sağ, Sol, Sağ, B, A. Test modu mühür sorularını atlar.",
            )
        elif self.game_state == "about":
            self.draw_information_page(
                "Kündekari hakkında",
                "Kündekari, küçük ahşap parçaların çivi ve tutkal kullanılmadan "
                "birbirine geçirilmesiyle yapılan geleneksel bir süsleme sanatıdır. "
                "Bu oyundaki sorular kündekari kültürel mirası hakkındadır.",
            )
        elif self.game_state in ("playing", "quiz", "paused", "dialog"):
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

        self.root.after(33, self.game_loop)


def main():
    root = tk.Tk()
    CippOyunu(root)
    root.mainloop()


if __name__ == "__main__":
    main()