import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, File } from 'lucide-react';
import Button from '@/components/common/Button';

interface DatasetUploadProps {
  onUpload: (file: File) => void;
  loading?: boolean;
}

export default function DatasetUpload({ onUpload, loading }: DatasetUploadProps) {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      onUpload(acceptedFiles[0]);
    }
  }, [onUpload]);

  const { getRootProps, getInputProps, isDragActive, acceptedFiles } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.ms-excel': ['.xls'],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
      'application/json': ['.json'],
    },
    maxFiles: 1,
    maxSize: 500 * 1024 * 1024,
  });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed rounded-xl p-12 text-center cursor-pointer transition-colors ${
        isDragActive ? 'border-primary-500 bg-primary-50' : 'border-gray-300 hover:border-primary-400'
      }`}
    >
      <input {...getInputProps()} />
      <Upload className="mx-auto text-gray-400 mb-4" size={48} />
      {isDragActive ? (
        <p className="text-primary-600 font-medium">Drop your file here...</p>
      ) : (
        <>
          <p className="text-gray-600 font-medium">Drag and drop your data file here</p>
          <p className="text-sm text-gray-400 mt-2">or click to browse (CSV, Excel, JSON, Parquet)</p>
          <p className="text-xs text-gray-400 mt-1">Max file size: 500 MB</p>
        </>
      )}
      {acceptedFiles.length > 0 && (
        <div className="mt-4 flex items-center justify-center gap-2 text-sm text-gray-600">
          <File size={16} />
          {acceptedFiles[0].name}
        </div>
      )}
    </div>
  );
}
