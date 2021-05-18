# Janus App

<img src="/fhir-mapper/images/logo.png" alt="logo" style="float: left; margin-right: 10px;" width="160"/> 
An extensible Python application that implements the FHIR® RESTful API to transform resources between different versions of FHIR or custom formats to FHIR.



## Info
This application is build with the Python Flask framework and implements a set of resources and interface interactions as defined by the HL7® FHIR® standard. It acts as a FHIR server and supports RESTful transactions using a HTTP request/response pattern. The primary focus of this API is to offer conversion capabilities and perform data transformations on the server-side. Currently, it converts from version STU3 to R4 of FHIR and supports the following resource types:
* AllergyIntolerance
* Bundle
* Composition
* Condition
* Device
* DeviceUseStatement
* DiagnosticReport
* ImagingStudy
* Immunization
* Media
* Medication
* MedicationStatement
* Observation
* Organization
* Patient
* Practitioner
* PractitionerRole
* Procedure
* Specimen

The scope covers the resource types used by the International Patient Summary (IPS). 

## Prerequisites
* Python >3.6
* Flask
* fhir.resources library

or

* Docker

## Usage
* Running via Python
    * Clone the repository.
    * Run `pip install -r requirements.txt` ideally inside a virtual environment.
    * The `.env` file contains the port where the webserver will be available.
    The default is set to `5000`, but can be customized.
    * Run `python fhir-mapper/fhir-mapper.py` and boot the server that runs on `http://0.0.0.0:5000/`.
* Running via Docker
    * Customize the webservers port inside the `.env` file or leave the default setting as is. This will also map the port from the container to the port in the host application.
    * Run `docker compose up`.

## License
* [MIT](https://tldrlegal.com/license/mit-license)

## Links
* [FHIR® standard](https://hl7.org/fhir/)
* [fhir.resources Python library](https://github.com/nazrulworld/fhir.resources)
* [International Patient Summary (IPS)](https://international-patient-summary.net/)
