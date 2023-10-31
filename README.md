# Weather Attribution Constrained Weather Generators (WGs) – Edwards Aquifer Authority (EAA) 9 Basins

This repository provides the source code for a custom weather generator (WG) that includes extreme events. A schematic for the WG framework is displayed below. The purpose of this WG framework is to enable calibration to drought magnitudes and likelihoods, under human induced climate change. After calibration, the attribution constrained WG will provide a climate description that provides increased probability of future occurrence for what was historically severe and extreme drought relative to Coupled Model Intercomparison Project (CMIP), global climate model (GCM) simulation results. 
<br/>
<figure>
    <img src="/assets/WG_Framework.png"
         width="1000"
         alt="Weather Generator with Events Schematic">
</figure>

<br/>

There are nine basins in the EAA study area as shown below. These basins were originally delineated for HSPF modeling.
<br/>
<figure>
    <img src="/assets/Study_Area-Full_Basins.png"
         width="1000"
         alt="EAA Nine Basins">
</figure>


## Source Code

The WG source code is available at [**src**](https://github.com/nmartin198/wattrib_wg_eaa/tree/main/src).


## Calibration Examples

Calibration examples are provided for each off the nine basins in [**calibration**](https://github.com/nmartin198/wattrib_wg_eaa/tree/main/calibration).


## Implementation Example

Implementation examples are provided for all nine basins in [**final**](https://github.com/nmartin198/wattrib_wg_eaa/tree/main/final).


## Extra Data

Daymet historical observations and LOCA2-downscaled, CMIP6 projected climate for emissions scenario ssp585 are available in  [**accessory_data**](https://github.com/nmartin198/wattrib_wg_eaa/tree/main/accessory_data).


## Example Plots and Calculations

Many of the plots and final calculations for this study were implemented in Jupyter Notebooks. These notebooks are available at   [**jupyter_notebooks**](https://github.com/nmartin198/wattrib_wg_eaa/tree/main/jupyter_notebooks).


## Author

* **Nick Martin** nick.martin@alumni.stanford.edu
<br/>

## License

This project is licensed under the GNU Affero General Public License v.3.0 - see the [LICENSE](LICENSE) file for details.
<br/>
