import matplotlib.pyplot as plt

def plot_red_flags(red_flags):
    """
    Plot financial red flags.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(red_flags["year"], red_flags["revenue_growth"])
    plt.title("Financial Red Flags: Revenue Growth")
    plt.xlabel("Year")
    plt.ylabel("Revenue Growth (%)")
    plt.show()