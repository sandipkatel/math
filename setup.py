import setuptools
  
setuptools.setup(
    name="math_equivalence",
    description="A utility for determining whether 2 answers for a problem in the MATH dataset are equivalent.",
    url="https://github.com/hendrycks/math",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "modeling"},
    py_modules = ["math_equivalence"],
)

# Run: python tune_gpt.py --mathematica-dataroot "1.0@C:/Users/Acer/Downloads/amps/amps/mathematica/" --khan-dataroot "1.0@C:/Users/Acer/Downloads/amps/amps/khan/" --MATH-dataroot "C:/Users/Acer/Downloads/MATH/" --tpu_num_cores 8
