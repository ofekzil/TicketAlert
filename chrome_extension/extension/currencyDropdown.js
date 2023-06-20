const currencies = Intl.supportedValuesOf("currency");
for (var currency of currencies) {
    document.write("<option>" + currency + "</option>");
}