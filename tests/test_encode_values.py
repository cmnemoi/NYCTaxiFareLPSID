from src.app.back import encode_values
import pandas as pd


def test_encode_creative_mobile_and_credit_card():
    test_data = pd.DataFrame(
        {
            "VendorID": ["Creative Mobile Technologies, LLC"],
            "payment_type": ["Carte de crédit"],
        }
    )
    result = encode_values(test_data.copy())
    assert result.loc[0, "VendorID"] == 1
    assert result.loc[0, "payment_type"] == 1


def test_encode_other_vendor_and_payment():
    test_data = pd.DataFrame({"VendorID": ["Other Vendor"], "payment_type": ["Cash"]})
    result = encode_values(test_data.copy())
    assert result.loc[0, "VendorID"] == 2
    assert result.loc[0, "payment_type"] == 2


def test_preserve_other_columns():
    test_data = pd.DataFrame(
        {
            "VendorID": ["Creative Mobile Technologies, LLC"],
            "payment_type": ["Carte de crédit"],
            "other_column": ["test"],
        }
    )
    result = encode_values(test_data.copy())
    assert "other_column" in result.columns
    assert result.loc[0, "other_column"] == "test"
