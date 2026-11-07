import pandapower as pp

# 1. Bikin wadah jaringan kosong
net = pp.create_empty_network()

# 2. Bikin 2 titik koneksi (Bus) dengan tegangan 20 kV (Tegangan Menengah)
bus_sumber = pp.create_bus(net, vn_kv=20.0, name="Bus Gardu")
bus_beban = pp.create_bus(net, vn_kv=20.0, name="Bus Pelanggan")

# 3. Pasang Sumber Listrik Utama (External Grid) di Bus Gardu
pp.create_ext_grid(net, bus=bus_sumber, name="PLN / Grid Utama")

# 4. Hubungkan kedua bus pakai Kabel standar sepanjang 1 km
pp.create_line(net, from_bus=bus_sumber, to_bus=bus_beban, length_km=1.0, 
               std_type="NAYY 4x150 SE", name="Kabel Distribusi")

# 5. Pasang Beban sebesar 2 Megawatt (MW) di Bus Pelanggan
pp.create_load(net, bus=bus_beban, p_mw=2.0, q_mvar=0.5, name="Beban Pabrik")

# 6. Jalankan kalkulasi aliran daya (Power Flow)
pp.runpp(net)

# 7. Cetak hasil tegangan di masing-masing bus
print("=== HASIL TEGANGAN BUS ===")
print(net.res_bus[['vm_pu', 'va_degree']])
