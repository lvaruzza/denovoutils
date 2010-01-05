//variables related to XMLHttpRequest
var xmlHttpRequest;

//variables related to VelvetMem Calculator
var readSize = 0; //Read size in bp (base pairs)
var genomeSize = 0; //Genome size in Mbp (megabase pairs)
var numReads = 0; //Number of reads in millions
var k = 0; //k-mer size (parameter of Velvet)
var mem = 0;
var mem_gb = 0;
var cov = 0;

//VelvetMem Calc function
function VelvetMemCalculator (read_size,genome_size,num_reads,kmer)
{
	mem = (-109635) + (18977*read_size) + (86326*genome_size) + (233353*num_reads) - (51092*kmer);
	mem_gb = Math.ceil((mem/(1024.0*1024)));
	cov = (read_size*num_reads*1.0)/genome_size;
	
	document.getElementById("velvetMem").style.visibility = "visible";	
	document.getElementById("spMemory").innerHTML = "<b>" + mem_gb + "</b>";
	document.getElementById("spCoverage").innerHTML = "<b>" + cov + "</b>";
	//alert("mem = " + mem_gb);
}		

function launchVelvetMem () {
	readSize = document.getElementById("txtReadSize");
	genomeSize = document.getElementById("txtGenomeSize");
	numReads = document.getElementById("txtNumReads");
	k = document.getElementById("txtK");

    VelvetMemCalculator(readSize.value,genomeSize.value,numReads.value,k.value);

}



