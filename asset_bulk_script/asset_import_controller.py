from flask import Flask

from oto.adaptors.flask import flaskify

from asset_bulk_script.api import app

from asset_bulk_script import config

from asset_bulk_script.logic import hello

def init_mapping():
    return ""

@app.route('/labels/mapping')
def label_mapping():
    return "Bleh"

@app.route('/assets/import/{label_id}')
def import_assets():
    init_mapping()

@app.route(config.HEALTH_CHECK, methods=['GET'])
def health():
    """Check the health of the application."""

    return flaskify(hello.health_check())

    #     if (jobQueue == null) {
    #         jobQueue = new ConcurrentLinkedQueue<>();
    #     }
    #
    #     LabelMapping mapping = labelMappingRepository.findOne(labelId);
    #
    #     if (mapping == null || mapping.getVendorId() == 0) {
    #         ResponseEntity<String> response = new ResponseEntity("Label ID "+labelId+" cannot be mapped to an Orchard Vendor ID", HttpStatus.BAD_REQUEST);
    #         return response;
    #     }
    #
    #     LabelStatus labelStatus = labelStatusRepository.findOne(labelId);
    #
    #     if (labelStatus != null && labelStatus.getStatus().equals("Transferring")) {
    #         return new ResponseEntity("Label already transferring. Check /assets/status/"+mapping.getLabelId()+" for Status", HttpStatus.OK);
    #     } else if (labelStatus == null) {
    #         labelStatus = new LabelStatus(labelId);
    #     }
    #     labelStatus.setStatus("Transferring");
    #     labelStatusRepository.save(labelStatus);
    #
    #     addImportJob(labelId, mapping.getVendorId(), reuploadTimedout, updateAssets);
    #
    #     runImportJobQueue();
    #
    #     ResponseEntity<String> response = new ResponseEntity("Job created. Check /assets/status/"+mapping.getLabelId()+" for Status", HttpStatus.OK);
    #     return response;
    # }

    # private synchronized  void addImportJob(String labelId, int vendorId, boolean reuploadTimedout, boolean updateAssets) {
    #     if (!containsJob(jobQueue, labelId)) {
    #         System.out.println("Adding new Job: "+labelId);
    #         jobQueue.add(new ImportJob(labelId, vendorId, reuploadTimedout, updateAssets));
    #         System.out.println("Now "+jobQueue.size()+" Jobs");
    #     }
    # }

    # private void runImportJobQueue() {
    #     if (importThread == null) {
    #         importThread = new Thread(new Runnable() {
    #             @Override
    #             public void run() {
    #                 while (true) {
    #                     startAvailableJobs(jobQueue);
    #                     try {
    #                         Thread.sleep(1000);
    #                     } catch (InterruptedException e) {
    #                         e.printStackTrace();
    #                     }
    #                 }
    #             }
    #         });
    #         importThread.start();
    #     }
    # }
    #
    # private synchronized  void startAvailableJobs(ConcurrentLinkedQueue<ImportJob> jobQueue) {
    #     long activeJobs = countActiveJobs(jobQueue);
    #     if (activeJobs < MAX_PARALLEL_JOBS) {
    #         ImportJob importJob = jobQueue.stream().filter(job -> !job.isActive()).findFirst().orElse(null);
    #
    #         if (importJob != null) {
    #             importJob.setActive(true);
    #
    #             String labelId = importJob.getLabelId();
    #             int vendorId = importJob.getVendorId();
    #             boolean reuploadTimedout = importJob.isReuploadTimedout();
    #             boolean updateAssets = importJob.isUpdateAssets();
    #
    #             System.out.println(labelId+" started");
    #
    #             Thread thread = new Thread(new Runnable() {
    #                 @Override
    #                 public void run() {
    #                     try {
    #                         AutomaticAssetImporter automaticAssetImporter = new AutomaticAssetImporter(importedProductRepository);
    #                         automaticAssetImporter.transferLabel(finetunesAWSDetails, labelId, vendorId, reuploadTimedout, updateAssets);
    #
    #                         LabelStatus labelStatus = labelStatusRepository.findOne(labelId);
    #                         labelStatus.setStatus("Done");
    #                         labelStatusRepository.save(labelStatus);
    #                     } catch (Exception e) {
    #                         LabelStatus labelStatus = labelStatusRepository.findOne(labelId);
    #                         labelStatus.setStatus("Exception: " + e.getMessage());
    #                         labelStatusRepository.save(labelStatus);
    #                     } finally {
    #                         System.out.println("Removing "+importJob.getLabelId());
    #                         jobQueue.remove(importJob);
    #                     }
    #                 }
    #             });
    #
    #             thread.start();
    #         }
    #     } else {
    #         System.out.println("Jobqueue currently too busy: "+activeJobs+" active Jobs");
    #     }
    # }
    #
    # private synchronized boolean containsJob(Queue<ImportJob> queue, String labelId) {
    #     if (queue == null || queue.size() == 0) {
    #         return false;
    #     }
    #     return queue.stream().map(job -> job.getLabelId()).filter(id -> id.equals(labelId)).count() > 0;
    # }
    #
    # private synchronized  long countActiveJobs(Queue<ImportJob> jobList) {
    #     return jobList.stream().filter(job -> job.isActive()).count();
    # }
    #
    # @RequestMapping("/assets/status/{label_id}")
    # public ResponseEntity<List<ProductStatus>> checkStatus(@PathVariable(value = "label_id", required=true) String labelId)
    # {
    #     try {
    #         List<ProductStatus> productStatuses = new ArrayList<>();
    #
    #         LabelMapping labelMapping = labelMappingRepository.findOne(labelId);
    #
    #         int vendorId = 0;
    #         if (labelMapping != null) {
    #             vendorId = labelMapping.getVendorId();
    #         } else {
    #             vendorId = Integer.parseInt(labelId);
    #         }
    #
    #         ProductListing productListing = ApiConnector.getProducts(vendorId);
    #
    #         for (ProductItem productItem : productListing.getItems()) {
    #             productStatuses.add(ApiConnector.getProductStatus(productItem.getProduct_id()));
    #         }
    #
    #         return new ResponseEntity<List<ProductStatus>>(productStatuses, HttpStatus.OK);
    #     } catch (Exception e) {
    #         e.printStackTrace();
    #         return new ResponseEntity<List<ProductStatus>>(new ArrayList<>(), HttpStatus.INTERNAL_SERVER_ERROR);
    #     }
    # }
    #
    # private void initMapping() {
    #     try {
    #         List<LabelMapping> dbMapping = labelMappingRepository.findAll();
    #
    #         Map<String, String> mapping = LabelExcelLoader.loadLabelMapping(new File("src/main/resources/finetunes_to_orchard_labelids.xls"));
    #
    #         if (dbMapping.isEmpty()) {
    #             for (String labelId : mapping.keySet()) {
    #                 LabelMapping labelMapping = new LabelMapping(labelId, Integer.parseInt(mapping.get(labelId)));
    #                 labelMappingRepository.save(labelMapping);
    #             }
    #         }
    #     } catch (Exception e) {
    #         e.printStackTrace();
    #     }
    # }