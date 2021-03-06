import Data.Map
import System.Environment

counter [] m = m
counter [x] m = Data.Map.insertWith (+) x 1 m
counter (x:xs) m = counter xs (Data.Map.insertWith (+) x 1 m)

main = do
  i <- readFile "day_2_testinput"

  let count = Prelude.fmap (\x -> counter x Data.Map.empty) $ lines i
  let twos = Prelude.fmap (\x -> Data.Map.filter (==2) x) $ count
  putStrLn $ show twos

