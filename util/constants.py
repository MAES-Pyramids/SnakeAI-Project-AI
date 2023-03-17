class CONSTANTS:
    WINDOW_TITLE = "Snake AI - Best game in the world. Powered by AI"
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    PIXEL_SIZE = [20, 20]  # [30, 30]
    GRID_SIZE = (WINDOW_WIDTH // PIXEL_SIZE[0], WINDOW_HEIGHT // PIXEL_SIZE[1])

    # Time step for fixed update
    default_STEP = 110  # 140
    TIME_STEP = default_STEP

    FPS = 60
    NUM_OBSTACLES = 30  # 8
    Max_Obstacle_length = 20  # 8
