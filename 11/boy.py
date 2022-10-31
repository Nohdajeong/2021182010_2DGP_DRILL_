from pico2d import *

# event 정의
RD, LD, RU, LU, TIMER, AD = range(6)    # 타이머 이벤트 추가

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_a): AD
}


# state 구현 - 클래스 이용
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0    # 정지 상태
        self.timer = 1000   # 타이머 초기화

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1             # 시간 감소
        if self.timer == 0:         # 시간이 다 되면
            self.add_event(TIMER)   # 타이머 이벤트를 큐에 삽입

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')

        # 어떤 이벤트 때문에 RUN으로 들어왔는지 확인을 하고, 그 이벤트에 따라 실제 방향 결정
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        print('EXIT RUN')

        # run 상태를 나갈 때, 현재 방향 저장
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0  # 정지 상태

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x+25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '',
                                           self.x-25, self.y-25, 100, 100)


class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER AUTO_RUN')
        if event == AD:
            if self.face_dir == -1:
                self.x -= 1
            elif self.face_dir == 1:
                self.x += 1

    @staticmethod
    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.face_dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        print('DRAW AUTO_RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)

# 상태 변환
next_state = {
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, TIMER: RUN, AD: AUTO_RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, LD: RUN, RD: RUN, TIMER: AUTO_RUN, AD: IDLE}
}


class Boy:
    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):  # event : 키 입력
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []

        # 초기 상태 설정 및 entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # 만약 list q에 뭔가 들어있으면
            event = self.q.pop()    # 이벤트 확인
            self.cur_state.exit(self)   # 현재 상태 나감
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태 계산
            self.cur_state.enter(self, event)  # 다음 상태의 enter 수행

    def draw(self):
        self.cur_state.draw(self)
