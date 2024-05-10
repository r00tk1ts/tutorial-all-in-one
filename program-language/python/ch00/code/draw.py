import matplotlib.pyplot as plt

versions = ['0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6',
            '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7',
            '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12']
start_years = [1991, 1994, 1995, 1996, 1996.5, 1997, 1998, 1999,
               2000, 2001, 2002, 2003, 2004, 2006, 2008, 2010,
               2008, 2009, 2011, 2012, 2014, 2015, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
end_years = [3, 1, 1, 0.5, 0.5, 1, 1, 1,
             1, 1, 1, 2, 2, 2, 2, 10,
             1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1]

bar_height = 0.9
positions = range(len(versions))
features = [
          '',
          'Lambda/Map/Filter/Reduce',
          '',
          '',
          '',
          'Keyword arguments/complex numbers support/data hiding by name mangling',
          '',
          '',
          'List/garbage collector of collecting reference cycles',
          'PSF liccense',
          'Unification of types(written in C) and classes(written in Python)',
          '',
          '',
          'With',
          'Released to coincide with Python 3.0',
          '',
          'Print/Text/Remove backward-compatibility features',
          'Ordered Dictionary',
          '',
          '',
          '',
          '',
          'formatted string literals/asynchronous generators',
          'breakpoint()/-X dev',
          'Assignment expressions',
          'Dict union operators/a new parser based on PEG',
          'Structural Pattern Matching',
          'Exception Groups/Variadic generics',
          'Type parameter/Type statement']

plt.figure(figsize=(13,8))

for i, (version, feature, start, end) in enumerate(zip(versions, features, start_years, end_years)):
    plt.barh(version, end, left=start, height=bar_height)
    plt.text(start+end+0.2, i-0.2, feature, ha='left', va='center')

#plt.barh(positions, end_years, left=start_years, height=bar_height)
plt.yticks(positions, versions)
plt.xticks([x for x in range(1991,2041,2)])
plt.ylabel('Version')
plt.xlabel('Year')
plt.title('Python Version Timeline')
plt.grid(False)

plt.show()
