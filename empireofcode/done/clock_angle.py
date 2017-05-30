def clock_angle(time):
    time = str(time).split(":")
    ans = round(abs((int(time[0]) * 30 + int(time[1]) * 0.5) - (int(time[1]) * 6)), 1)
    return abs(min(360 - ans, ans))


"""
Clock Angle

How do we measure an angle without a protractor? Sometime in battles things get complicated and we need to use the 
things around us in creative ways. To get the degrees of an angle, a simple analog clock can help us out here.

Analog clocks display time with an analog clock face, which consists of a round dial with the numbers 1 through 12, 
the hours in the day, around the outside. The hours are indicated with an hour hand, which makes two revolutions 
in a day, while the minutes are indicated by a minute hand, which makes one revolution per hour. In this mission we 
will use a clock without second hand. The hour hand moves smoothly and the minute hand moves step by step.

You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in
degrees. Don't forget that clock has numbers from 1 to 12, so 23 == 11. The time is given as a string with the follow 
format "HH:MM", where HH is hours and MM is minutes. Hours and minutes are given in two digits format, so "1" will be 
writen as "01". The result should be given in degrees with precision ±0.1.


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

Example:

clock_angle("02:30") == 105
clock_angle("13:42") == 159
clock_angle("01:43") == 153.5
Precondition:

Input time matches by regexp expression "\A((2[0-3])|([0-1][0-9])):[0-5][0-9]\Z"

How it is used:

Simple mathematics and skill to built a model for various things from real world.


"""
print(clock_angle("18:00"))
