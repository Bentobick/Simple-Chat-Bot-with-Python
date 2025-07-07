spinInput = input()
electricChargeInput = input()

if spinInput == "1/2":
    if spinInput == "1/2" and electricChargeInput == "0":
        print("Neutrino Lepton")
    elif spinInput == "1/2" and electricChargeInput == "-1":
        print("Electron Lepton")
    elif spinInput == "1/2" and electricChargeInput == "2/3":
        print("Charm Quark")
    elif spinInput == "1/2" and electricChargeInput == "-1/3":
        print("Strange Quark")
    else:
        print("There is no matching particle and class for your input.")
elif spinInput == "1" and electricChargeInput == "0":
    print("Photon Boson")
else:
    print("There is no matching particle and class for your input.")
