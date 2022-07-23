# CodeUp 2632 : 계단 오르기 1
# n번 = n-1번 계단을 한번 오르는 수 + n-2번 계단을 두번 오르는 수이다.

n = int(input())

history_climb = []

def cnt_climb_set(cnt, history_climb) : #{
    if cnt == n : #{
      print(sum(history_climb))
      return

    else : #{
        cnt_climb_set(cnt+1, [history_climb[1], sum(history_climb)])
    #}
#}

cnt_climb_set(1, [0, 1])