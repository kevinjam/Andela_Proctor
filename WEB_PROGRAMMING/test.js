describe("test for longest function functionality", function() {
  it("should return correct output for normal strings", function() {
    expect(longest("A")).toEqual("A");
    expect(longest("I love Avatar")).toEqual("Avatar");
    expect(longest("The stupidities of youth")).toEqual("stupidities");
  });

  it("should return correct output for gibberish", function() {
    expect(longest("hgdydrxtfEq Rradsc tstsa taeWwwec fgdd")).toEqual("hgdydrxtfEq");
  });

  it("should work for sentences with numbers", function() {
    expect(longest("This is a sentence with a number 7685838788")).toEqual("7685838788");
  });
});