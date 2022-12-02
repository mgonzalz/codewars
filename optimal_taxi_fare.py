def calculate_optimal_fare(d, t, v1, r, v2): #dividido por 60 para pasarlo a minutos
    kmmin = (d/t)
    if kmmin<=v2/60:
        return "0.00"
    elif kmmin > v1/60:
        return "Won't make it!"
    
    return f"{r*(v1/60)*(d-(v2/60)*t)/((v1/60)-v2/60):.2f}"

