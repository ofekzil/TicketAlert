const currencies = Intl.supportedValuesOf("currency");
for (var currency of currencies) {
    if (currency === "USD") {
        document.write("<option selected='selected'>" + currency + "</option>");
    } else { 
        document.write("<option>" + currency + "</option>");
    }
}