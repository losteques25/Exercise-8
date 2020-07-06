d={"Valencia":794000, "Salamanca":144000, "Cadiz":116000, "Madrid":3200000}
capitals={key:val for key, val in d.items() if val>200000}
print(sort.capitals)
