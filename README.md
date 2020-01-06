# Link-invalidation-project

The aim of this project is to develop a simple tool that help to detect incorrect sameAs links by using the functionality degree of the properties. This degree has to be computed by your tool in one dataset and then used to detect dissimilar property values for the functional properties that describe two URIs of two datasets (very simple inspiration from Papaleo et al 2014).

The RDF dataset with its corresponding OWL ontology:

IIMB datasets are available here: link

Choose OWL datatrack IIMB large.

There are many versions of the dataset, owl ontology with their instances (file OWL of the folders 000, 001 ….).

Refalign in folder 001 is the gold standard (the set of correct owl:sameAs links between the data in 000 and the ones in 001).

Take the first dataset (000) and extract the functional properties (i.e. compute the degree of functionality of each property and select the ones having a very high degree according to a fixed threshold. Then, develop a simple invalidation tool based on these functional properties.

For the evaluation of your tool, you may inject random erroneous sameAs links for the class Film in the refalign and check whether your tool finds these erroneous links (recall and precision measures)

A library of a bench of similarity measures: Second String distance. You may find additional details on here
