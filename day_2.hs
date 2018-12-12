import Data.Map
import System.Environment

counter [] m = m
counter [x] m = Data.Map.insertWith (+) x 1 m
counter (x:xs) m = counter xs (Data.Map.insertWith (+) x 1 m)


