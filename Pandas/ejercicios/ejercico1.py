from unittest.mock import MagicMock
import pandas as pd
pd.Series = MagicMock()

recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}
