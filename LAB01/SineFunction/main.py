import matplotlib.pyplot as plt
import pandas as pd

def main():
    degrees,sine,taylor_polynomial,reduced_taylor_polynomial = read_excel()
    draw_func(degrees,sine,taylor_polynomial,reduced_taylor_polynomial)

def read_excel():
    df = pd.read_excel(r"..\SineFunction.xlsx", header=3)
    degrees = df["Degree"]
    sine = df["Sine"]
    taylor_polynomial = df["TaylorPolyn."]
    reduced_taylor_polynomial = df["ReducedTaylorPolyn."]

    return degrees,sine,taylor_polynomial,reduced_taylor_polynomial

def draw_func(degrees,sine,taylor_polynomial,reduced_taylor_polynomial):
    plt.plot(degrees,sine, label="Sine")
    plt.plot(degrees,taylor_polynomial, label="Taylor Polynomial")
    plt.plot(degrees,reduced_taylor_polynomial, label="Reduced Taylor Polynomial")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
     main()