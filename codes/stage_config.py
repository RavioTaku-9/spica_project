from config import IMAGE_DIR
 
class StageConfig:
    def __init__(self, name, bg_index, difficulty=1.0):
        self.name = name
        self.bg_index = bg_index
        self.difficulty = difficulty  # 敵の強さ倍率

 
# ステージ定義
STAGES = [
    StageConfig("Night Town", 0,  difficulty=1.0),
    StageConfig("Twilight", 1,  difficulty=1.2),
    StageConfig("Snow Mountain", 2, difficulty=1.5),
    StageConfig("Day Town", 3, difficulty=1.8),
    StageConfig("Museum", 4, difficulty=2.0),
]