
import collections

sonnet_1 = ["from", "fairest", "creatures", "we", "desire", "increase",
            "that", "thereby", "beauty","rose", "might","never", "die",
            "but", "as", "the", "riper", "should", "by","time", "decease",
            "his", "tender", "heir", "might", "bear", "his", "memory", "but",
            "thou", "contracted", "to", "thine", "own", "bright", "eyes", "feed",
            "thy","light", "flame", "with", "self-substantial", "fuel", "making", "a",
            "famine", "where", "abundance", "lies", "thyself", "thy", "foe" ,"to", "thy",
            "sweet", "self", "too", "cruel"]

frequency = collections.Counter(sonnet_1)

print(frequency)

print("---------------------------------------------------------------------------------------")

print(frequency.keys())

