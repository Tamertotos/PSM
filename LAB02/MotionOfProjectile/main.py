import matplotlib.pyplot as plt


def main():
    euler_method()






def euler_method():
    sx, sy, vx, vy, gx, gy, dt = 0, 0, 10, 10, 0, -10, 0.1

    x,y = [sx], [sy]
    while sy >= 0:
        sx = sx + vx * dt
        sy = sy + vy * dt
        vx = vx + gx * dt
        vy = vy + gy * dt
        x.append(sx)
        y.append(sy)
    fig = plt.figure(figsize= (15, 5))
    plt.plot(x,y, marker="o", c="blue", mfc="red")
    plt.grid(True, which="both")
    plt.axis((0,25,0,6))
    plt.show()

if __name__ == "__main__":
    main()